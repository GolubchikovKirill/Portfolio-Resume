"""
Нужно реализовать систему для управления библиотекой с помощью классов
"""
class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
        self.is_checked_out = False  # Статус книги: False — в библиотеке, True — выдана

    def __str__(self):
        status = "взята" if self.is_checked_out else "в наличии"
        return f"{self.title} ({self.author}, {self.year}) - {status}"


class Library:
    def __init__(self):
        """
        Инициализация библиотеки.
        """
        self.books: list[Book] = []  # Список для хранения объектов класса Book.

    def add_book(self, book: Book) -> None:
        """
        Добавление новой книги в библиотеку.
        """
        self.books.append(book)
        print(f"Книга '{book.title}' добавлена в библиотеку.")

    def remove_book(self, title: str) -> None:
        """
        Удаление книги по названию.
        """
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Книга '{title}' удалена из библиотеки.")
                return
        print(f"Книга '{title}' не найдена в библиотеке.")

    def checkout_book(self, title: str) -> None:
        """
        Выдача книги пользователю.
        """
        for book in self.books:
            if book.title == title:
                if book.is_checked_out:
                    print(f"Книга '{title}' уже взята.")
                else:
                    book.is_checked_out = True
                    print(f"Книга '{title}' успешно выдана.")
                return
        print(f"Книга '{title}' не найдена в библиотеке.")

    def return_book(self, title: str) -> None:
        """
        Возврат книги в библиотеку.
        """
        for book in self.books:
            if book.title == title:
                if book.is_checked_out:
                    book.is_checked_out = False
                    print(f"Книга '{title}' успешно возвращена.")
                else:
                    print(f"Книга '{title}' уже была в библиотеке.")
                return
        print(f"Книга '{title}' не найдена в библиотеке.")

    def display_books(self) -> None:
        """
        Отображение всех книг в библиотеке с их статусами.
        """
        if not self.books:
            print("Библиотека пуста.")
            return
        print("Книги в библиотеке:")
        for book in self.books:
            print(f"  - {book}")


# Пример использования библиотеки
library = Library()

# Добавляем книги
library.add_book(Book("1984", "George Orwell", 1949))
library.add_book(Book("Brave New World", "Aldous Huxley", 1932))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 1960))

# Отображаем все книги
library.display_books()

# Выдаем книгу
library.checkout_book("1984")
library.display_books()

# Возвращаем книгу
library.return_book("1984")
library.display_books()

# Удаляем книгу
library.remove_book("Brave New World")
library.display_books()



    



    

        