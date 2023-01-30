BOOKS_DATABASE = [
    {
        "id_": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id_": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге

        """
        if not isinstance(id_, int):
            raise TypeError("идентификатор книги должен быть типа int")
        if id_ <= 0:
            raise ValueError("идентификатор книги должен быть положительным числом")
        self.id_ = id_

        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Количество страниц в книге должно быть типа int")
        if pages < 0:
            raise ValueError("Количество страниц в книге не может быть отрицательным числом")
        self.pages = pages


class Library:
    def __init__(self, books = []):
        """
        Создание и подготовка к работе объекта "Библиотека"

        :param books: Список книг

        """
        self.books = books

    def get_next_book_id_(self):
        """
        Функция. которая возвращает идентификатор для добавления новой книги в библиотеку

        :return: Идендификатор

        """
        if not self.books:
            return 1
        return self.books[-1].id_ + 1

    def get_index_by_book_id_(self, id_: int):
        """
        Функция. которая возвращает индекс книги в списке, который хранится в атрибуте экземпляра класса

        :raise ValueError: Если книги нет, то вызываем ошибку с сообщением : "Книги с запрашиваемым id не существует"

        :return: Индекс книги

        """
        if not isinstance(id_, int):
            raise TypeError("Идентификатор книги должен быть типа int")
        if id_ <= 0:
            raise ValueError("Идентификатор книги должен быть положительным числом")
        self.id_ = id_

        for i, book in enumerate(self.books):
            if book.id_ == id_:
                return i
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id_())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id_"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id_())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id_(1))  # проверяем индекс книги с id = 1
# Последняя строка