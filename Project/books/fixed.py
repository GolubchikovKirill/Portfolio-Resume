from ebooklib import epub


def fix_epub_structure(epub_path, fixed_epub_path):
    """
    Исправляет структуру EPUB, добавляя недостающие файлы в манифест.
    :param epub_path: Исходный EPUB-файл.
    :param fixed_epub_path: Путь к исправленному EPUB-файлу.
    """
    try:
        book = epub.read_epub(epub_path)

        # Добавление недостающих метаданных
        if not book.get_metadata('DC', 'title'):
            book.set_title("Untitled Book")
        if not book.get_metadata('DC', 'language'):
            book.set_language("en")
        
        # Проверяем наличие всех файлов
        for item in book.items:
            if item.file_name.startswith("images/") and not item.content:
                print(f"Изображение {item.file_name} отсутствует.")
                # Можно удалить или заменить недостающий файл

        epub.write_epub(fixed_epub_path, book)
        print(f"Исправленный файл сохранён: {fixed_epub_path}")

    except Exception as e:
        print(f"Ошибка при исправлении EPUB: {e}")


# Пример использования
fix_epub_structure("Марк Лутц Изучаем Python 2.epub", "Марк Лутц Изучаем Python 2_fixed.epub")