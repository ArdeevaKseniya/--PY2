class Tea:
    """ Базовый класс чай. """

    def __init__(self, country: str, kind_of_tea: str, price: float):
        """
        Создание и подготовка к работе объекта "Чай"

        :param country: Страна, где производится данный чай
        :param kind_of_tea: Вид чая (зеленый, черный)
        :param price: Цена чая

        """
        self._country = country
        self.kind_of_tea = kind_of_tea
        self._price = price

    @property
    def country(self) -> str:
        """Возвращает страну, где производится данный чай. Не позволяет изменять атрибут"""
        return self._country

    @property
    def price(self) -> float:
        """Возвращает цену за чай. Не позволяет изменять атрибут"""
        return self._price

    @price.setter
    def price(self, price: float) -> None:
        """Устанавливает цену, накладывает ограничения по типу и допустимым значениям."""
        if not isinstance(price, float):
            raise TypeError("Цена чая должна быть типа float")
        if price <= 0:
            raise ValueError("Цена чая должна быть положительным числом")
        self._price = price

    def __str__(self):
        """
        Функция. которая возвращает строку формата, где "Страна", "Вид_чая" и "Цена_чая" берутся с помощью
        атрибутов country, kind_of_tea и price

        :return: Строка со страной, видом чая и его ценой с помощью атрибутов country, kind_of_tea и price

        """
        return f"Страна {self._country}. Вид чая {self.kind_of_tea}. Цена {self._price}"

    def __repr__(self):
        """
        Функция. которая возвращает валидную python строку, по которой можно инициализировать точно такой же экземпляр

        :return: Валидная python строка

        """
        return f"{self.__class__.__name__}(country={self._country!r}, kind_of_tea={self.kind_of_tea!r}, \
        price={self._price!r})"

    def russian_production(self) -> None:
        """
        Функция, которая проверяет, что производство чая ведется в России

        :raise ValueError: Если страна производства чая не Россия, то вызываем ошибку

        """
        ...

    def buying_tea(self, money: float) -> None:
        """
        Функция, которая проверяет возможность покупателя оплатить покупку чая

        :param money: Количество денег в кошельке покупателя

        :raise ValueError: Если цена за чай превышает количество денег в кошельке покупателя, то вызываем ошибку

        """
        if not isinstance(money, (int, float)):
            raise TypeError("Количество денег в кошельке покупателя должно быть типа int или float")
        if money <= 0:
            raise ValueError("Количество денег в кошельке покупателя должно быть положительным числом")
        ...


class TeaSachets(Tea):
    """ Дочерний класс чай. Чай в пакетиках. """

    def __init__(self, country: str, kind_of_tea: str, price: float, number_of_sachets: int):
        """
        Создание и подготовка к работе объекта "Чай в пакетиках"

        :param country: Страна, где производится данный чай
        :param kind_of_tea: Вид чая (зеленый, черный)
        :param price: Цена чая
        :param number_of_sachets: Количество пакетиков чая в упаковке

        """
        super().__init__(country, kind_of_tea, price)
        self._number_of_sachets = number_of_sachets

    @property
    def number_of_sachets(self) -> int:
        """Возвращает количество пакетиков."""
        return self._number_of_sachets

    @number_of_sachets.setter
    def number_of_sachets(self, number_of_sachets: int) -> None:
        """Устанавливает количество пакетиков, накладывает ограничения по типу и допустимым значениям."""
        if not isinstance(number_of_sachets, int):
            raise TypeError("Количество пакетиков должно быть типа int")
        if number_of_sachets <= 0:
            raise ValueError("Количество пакетиков должно быть положительным числом")
        self._number_of_sachets = number_of_sachets

    def __repr__(self):
        """
        Функция. которая возвращает валидную python строку, по которой можно инициализировать точно такой же экземпляр.
        Перегружаем метод, так как появился новый атрибут

        :return: Валидная python строка

        """
        return f"{self.__class__.__name__}(country={self._country!r}, kind_of_tea={self.kind_of_tea!r}, \
        price={self._price!r}, number_of_sachets={self._number_of_sachets!r})"


class LeafTea(Tea):
    """ Дочерний класс чай. Чай в пакетиках. """

    def __init__(self, country: str, kind_of_tea: str, price: float, number_of_grams: float):
        """
        Создание и подготовка к работе объекта "Чай в пакетиках"

        :param country: Страна, где производится данный чай
        :param kind_of_tea: Вид чая (зеленый, черный)
        :param price: Цена чая
        :param number_of_grams: Количество грамм чая

        """
        super().__init__(country, kind_of_tea, price)
        self._number_of_grams = number_of_grams

    @property
    def number_of_grams(self) -> float:
        """Возвращает количество грамм чая."""
        return self._number_of_grams

    @number_of_grams.setter
    def number_of_grams(self, number_of_grams: float) -> None:
        """Устанавливает количество грамм чая, накладывает ограничения по типу и допустимым значениям."""
        if not isinstance(number_of_grams, float):
            raise TypeError("Количество грамм чая должно быть типа float")
        if number_of_grams <= 0:
            raise ValueError("Количество грамм чая должно быть положительным числом")
        self._number_of_grams = number_of_grams

    def __repr__(self):
        """
        Функция. которая возвращает валидную python строку, по которой можно инициализировать точно такой же экземпляр.
        Перегружаем метод, так как появился новый атрибут

        :return: Валидная python строка

        """
        return f"{self.__class__.__name__}(name={self._country!r}, kind_of_tea={self.kind_of_tea!r}, \
        price={self._price!r}, number_of_grams={self._number_of_grams!r})"

    def buying_tea(self, money: float) -> None:
        """
        Функция, которая проверяет возможность покупателя оплатить чай.
        Перегружаем метод, так как нужно пересчитать цену за чай. Цена указана только за 100 грамм чая.

        :param money: Количество денег в кошельке покупателя

        :raise ValueError: Если цена за чай превышает количество денег в кошельке покупателя, то вызываем ошибку

        """
        if not isinstance(money, float):
            raise TypeError("Количество денег в кошельке покупателя должно быть типа float")
        if money <= 0:
            raise ValueError("Количество денег в кошельке покупателя должно быть положительным числом")
        ...


if __name__ == "__main__":
    print(Tea("Россия", "Черный", 450))
    print(TeaSachets("Россия", "Черный", 450, 25))
    print(LeafTea("Россия", "Черный", 450, 150))
# Последняя строка
