import fitz  # PyMuPDF
from ebooklib import epub
import os
import requests
from PIL import Image
from io import BytesIO
import logging

# Настройка логирования
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Функция для скачивания изображения
def download_image(url, save_path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
        else:
            logger.error(f"Ошибка скачивания изображения {url}: {response.status_code}")
    except Exception as e:
        logger.error(f"Не удалось скачать изображение {url}: {e}")

# Функция для извлечения текста и изображений из PDF
def extract_text_and_images(pdf_path):
    doc = fitz.open(pdf_path)
    images = []
    text = ""
    
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        try:
            page_text = page.get_text("html")  # Извлекаем текст в HTML формате
            if not page_text.strip():
                logger.warning(f"Текст на странице {page_num + 1} не был извлечен корректно.")
            text += page_text
        except Exception as e:
            logger.error(f"Ошибка при извлечении текста с страницы {page_num + 1}: {e}")
        
        # Извлекаем изображения
        for img_index, img in enumerate(page.get_images(full=True)):
            try:
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_data = base_image["image"]
                img_filename = f"image_{page_num + 1}_{img_index + 1}.png"
                with open(img_filename, 'wb') as img_file:
                    img_file.write(image_data)
                images.append(img_filename)
            except Exception as e:
                logger.error(f"Ошибка при извлечении изображения с страницы {page_num + 1}: {e}")
    
    return text, images

# Функция для извлечения первой страницы как изображения (обложка)
def extract_cover_image(pdf_path, cover_image_path):
    try:
        doc = fitz.open(pdf_path)
        page = doc.load_page(0)  # Первая страница
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # Увеличиваем разрешение для лучшего качества
        pix.save(cover_image_path)
        logger.info(f"Обложка извлечена и сохранена как {cover_image_path}")
    except Exception as e:
        logger.error(f"Не удалось извлечь обложку: {e}")

# Функция для исправления простых ошибок HTML-разметки
def fix_html_content(html_content):
    try:
        # Простейшие исправления, например, добавление закрывающих тегов
        html_content = html_content.replace("<html><body>", "<html><head><style>body{font-family: Arial, sans-serif;}</style></head><body>\n")
        html_content = html_content.replace("</body></html>", "\n</body></html>")
        
        # Добавление стилей для улучшения отображения
        if "<style>" not in html_content:
            html_content = "<style>body { font-family: Arial, sans-serif; line-height: 1.5; margin: 0; padding: 0; }</style>" + html_content
        
        # Очистка избыточных тегов
        html_content = html_content.replace("<p></p>", "")  # Удаление пустых параграфов
        html_content = html_content.replace("<br>", "<br/>")  # Стандартизация тегов переноса
        
        return html_content
    except Exception as e:
        logger.error(f"Ошибка при исправлении HTML-контента: {e}")
        return html_content  # В случае ошибки возвращаем исходный контент

# Функция для создания EPUB
def create_epub(pdf_path, output_epub, author="Unknown", title="Converted Book"):
    try:
        # Путь для сохранения обложки
        cover_image_path = "cover_image.jpg"
        
        # Извлекаем первую страницу PDF как изображение (обложка)
        extract_cover_image(pdf_path, cover_image_path)
        
        # Извлекаем текст и изображения из PDF
        text, images = extract_text_and_images(pdf_path)
        
        # Если текст не был извлечен или изображений нет, выводим предупреждение
        if not text:
            logger.warning("Текст из PDF не был извлечен или извлечен некорректно.")
        if not images:
            logger.warning("Изображения не были извлечены или извлечены некорректно.")
        
        # Создаем книгу EPUB
        book = epub.EpubBook()
        
        # Устанавливаем мета-данные (автор, название)
        book.set_identifier('id123456')
        book.set_title(title)
        book.set_language('en')
        book.add_author(author)

        # Добавляем извлеченную обложку в EPUB
        with open(cover_image_path, 'rb') as cover_file:
            cover_content = cover_file.read()
            cover_item = epub.EpubItem(
                uid="cover",
                file_name="cover.jpg",
                media_type="image/jpeg",
                content=cover_content
            )
            book.add_item(cover_item)
            book.set_cover("cover.jpg", cover_content)

        # Создаем первую страницу с текстом
        content = fix_html_content(f"<html><body>{text}</body></html>")
        page = epub.EpubHtml(title='Page 1', file_name='page1.xhtml', lang='en')
        page.set_content(content)
        book.add_item(page)

        # Добавляем изображения в EPUB
        for img_filename in images:
            try:
                img_item = epub.EpubItem(
                    uid=f"{img_filename}",
                    file_name=f"images/{img_filename}",
                    media_type="image/png",
                    content=open(img_filename, 'rb').read()
                )
                book.add_item(img_item)
            except Exception as e:
                logger.error(f"Ошибка при добавлении изображения {img_filename} в EPUB: {e}")

        # Добавляем таблицу содержимого (если нужно)
        book.spine = ['nav', page]

        # Добавление навигационного файла
        book.add_item(epub.EpubNav())

        # Сохраняем файл EPUB
        epub.write_epub(output_epub, book)
        
        # Удаляем временные изображения
        for img_filename in images:
            os.remove(img_filename)
        os.remove(cover_image_path)

        logger.info(f"Конвертация завершена. EPUB файл создан: {output_epub}")
    
    except Exception as e:
        logger.error(f"Ошибка при создании EPUB файла: {e}")

# Путь к PDF-файлу
pdf_file = "Лутц М. - Изучаем Python, том 1 - 2020.pdf"  # Укажите путь к вашему PDF файлу
output_epub = "Лутц М. - Изучаем Python, том 1 - 2020.epub"  # Укажите имя для выходного EPUB файла
author = "Марк Лутц"  # Укажите имя автора
title = "Изучаем Python том 1"  # Укажите название книги

# Конвертируем PDF в EPUB
create_epub(pdf_file, output_epub, author, title)
