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

    def __str__(self) -> str:
        """
        Функция. которая возвращает строку формата, где "название_книги" берется с помощью атрибута name

        :return: Строка с названием книги с помощью атрибута name

        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Функция. которая возвращает валидную python строку, по которой можно инициализировать точно такой же экземпляр

        :return: Валидная python строка

        """
        return f'Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})'


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id_"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
# Последняя строка