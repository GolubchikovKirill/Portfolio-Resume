import os
import fitz  # PyMuPDF
from ebooklib import epub


def extract_pdf_content_with_images(pdf_path, output_dir):
    """
    Извлекает текст и изображения из PDF.
    :param pdf_path: Путь к PDF-файлу.
    :param output_dir: Директория для сохранения извлечённых изображений.
    :return: Список страниц с текстом и список путей к изображениям.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    doc = fitz.open(pdf_path)
    pages_content = []  # Список для текста страниц
    image_files = []  # Список путей к извлечённым изображениям

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pages_content.append(page.get_text("text"))  # Извлечение текста

        # Извлечение изображений
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_filename = os.path.join(output_dir, f"page{page_num+1}_img{img_index+1}.{image_ext}")

            # Сохранение изображения
            with open(image_filename, "wb") as f:
                f.write(image_bytes)

            image_files.append(image_filename)

    return pages_content, image_files


def create_epub_with_images(title, pages, images, output_epub):
    """
    Создаёт EPUB с текстом и изображениями.
    :param title: Название книги.
    :param pages: Список текстов страниц.
    :param images: Список путей к изображениям.
    :param output_epub: Имя выходного EPUB файла.
    """
    book = epub.EpubBook()
    book.set_title(title)
    book.set_language("en")

    # Добавляем текстовые страницы
    for page_num, page_text in enumerate(pages, start=1):
        chapter = epub.EpubHtml(
            title=f"Page {page_num}",
            file_name=f"page_{page_num}.xhtml",
            content=f"<h1>Page {page_num}</h1><p>{page_text}</p>",
        )
        book.add_item(chapter)

    # Добавляем изображения
    for image_path in images:
        if os.path.exists(image_path):
            with open(image_path, "rb") as img_file:
                image_data = img_file.read()
            image_name = os.path.basename(image_path)
            epub_image = epub.EpubItem(
                uid=image_name,
                file_name=f"images/{image_name}",
                media_type=f"image/{image_name.split('.')[-1]}",
                content=image_data,
            )
            book.add_item(epub_image)

    # Определяем структуру книги
    book.toc = [epub.Link(ch.file_name, ch.title, ch.file_name) for ch in book.items if isinstance(ch, epub.EpubHtml)]
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # Устанавливаем стиль
    style = "body { font-family: Arial, sans-serif; }"
    nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
    book.add_item(nav_css)

    # Сохраняем книгу
    epub.write_epub(output_epub, book)
    print(f"EPUB успешно создан: {output_epub}")


# Основная функция
def pdf_to_epub(pdf_path, output_dir, output_epub):
    """
    Конвертирует PDF в EPUB с изображениями.
    :param pdf_path: Путь к PDF-файлу.
    :param output_dir: Директория для временных файлов.
    :param output_epub: Имя выходного EPUB файла.
    """
    if not os.path.exists(pdf_path):
        print(f"Файл {pdf_path} не найден.")
        return

    print("Извлечение содержимого из PDF...")
    pages, images = extract_pdf_content_with_images(pdf_path, output_dir)
    print("Содержимое извлечено.")

    print("Создание EPUB файла...")
    create_epub_with_images(title="Converted PDF to EPUB", pages=pages, images=images, output_epub=output_epub)
    print("EPUB файл создан.")


# Пример использования
pdf_path = "Лутц М. - Изучаем Python, том 2 - 2020.pdf"  # Ваш PDF файл
output_dir = "temp_images"  # Директория для временных изображений
output_epub = "Изучаем Python_2.epub"  # Имя выходного EPUB файла

pdf_to_epub(pdf_path, output_dir, output_epub)