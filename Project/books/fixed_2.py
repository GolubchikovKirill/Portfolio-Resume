import zipfile
import os
import shutil


def unpack_epub(epub_path, output_dir):
    """
    Распаковывает EPUB в указанную директорию.
    :param epub_path: Путь к EPUB-файлу.
    :param output_dir: Директория для распаковки.
    """
    if not os.path.exists(epub_path):
        print(f"Файл {epub_path} не найден.")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with zipfile.ZipFile(epub_path, 'r') as zip_ref:
        zip_ref.extractall(output_dir)
    print(f"EPUB распакован в {output_dir}")


def pack_epub(input_dir, output_epub):
    """
    Упаковывает директорию обратно в EPUB.
    :param input_dir: Директория с содержимым EPUB.
    :param output_epub: Имя выходного EPUB-файла.
    """
    if not os.path.exists(input_dir):
        print(f"Директория {input_dir} не найдена.")
        return

    with zipfile.ZipFile(output_epub, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
        for root, _, files in os.walk(input_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, input_dir)
                zip_ref.write(file_path, arcname)
    print(f"EPUB упакован в {output_epub}")


# Пример использования
unpack_epub("example.epub", "unpacked_epub")
# После исправлений
pack_epub("unpacked_epub", "repacked_example.epub")