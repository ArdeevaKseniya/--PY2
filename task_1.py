import doctest


class Card:
    def __init__(self, number_card: int, balance: int):
        """
        Создание и подготовка к работе объекта "Банковская карта"

        :param number_card: Номер карты
        :param balance: Баланс карты

        Примеры:
        >>> card = Card(6783927407564836, 5000)
        """
        if not isinstance(number_card, int):
            raise TypeError("Номер карты должен быть типа int")
        if number_card <= 0:
            raise ValueError("Номер карты должен быть положительным числом")
        self.number_card = number_card

        if not isinstance(balance, int):
            raise TypeError("Баланс карты должен быть int или float")
        if balance < 0:
            raise ValueError("Баланс карты не может быть отрицательным числом")
        self.balance = balance

    def amount_symbol_number(self, desired_number_card: int) -> None:
        """
        Функция, которая проверяет равно ли количество символов в карте необходимому количеству

        :param desired_number_card: Необходимое количество символов в номере карты

        :raise ValueError: Если количество символов в карте не равно необходиомому значению, то вызываем ошибку

        Примеры:
        >>> card = Card(6783927407564836, 5000)
        >>> card.amount_symbol_number(16)
        """
        if not isinstance(desired_number_card, int):
            raise TypeError("Номер карты должен быть типа int")
        if desired_number_card <= 0:
            raise ValueError("Номер карты должен быть положительным числом")
        ...

    def is_empty_balance(self) -> bool:
        """
        Функция которая проверяет является ли баланкс нулевым

        :return: Является ли баланс нулевым

        Примеры:
        >>> card = Card(6783927407564836, 5000)
        >>> card.is_empty_balance()
        """
        ...

class Headphones:
    def __init__(self, volume_level: int, charge_level: int):
        """
        Создание и подготовка к работе объекта "Наушники"

        :param volume_level: Уровень громкости наушников
        :param charge_level: Уровень заряда наушников в процентах

        Примеры:
        >>> headphones = Headphones(7, 70)
        """
        if not isinstance(volume_level, int):
            raise TypeError("Уровень громкости наушников должен быть типа int")
        if volume_level <= 0:
            raise ValueError("Уровень громкости наушников должен быть положительным числом")
        if volume_level > 10:
            raise ValueError("Уровень громкости наушников должен быть меньше или равен 10")
        self.volume_level = volume_level

        if not isinstance(charge_level, int):
            raise TypeError("Уровень заряда наушников в процентах должен быть int или float")
        if charge_level < 0:
            raise ValueError("Уровень заряда наушников в процентах не может быть отрицательным числом")
        if charge_level > 100:
            raise ValueError("Уровень заряда наушников в процентах должен быть меньше или равен 100")
        self.charge_level = charge_level

    def safe_listening(self) -> bool:
        """
        Функция, которая проверяет возможно ли при таком уровне громкости безопасное прослушивание музыки

        :return: Попадает ли уровень громкости в диапазон громкостей безопасного прослушивания музыки

        Примеры:
        >>> headphones = Headphones(7, 70)
        >>> headphones.safe_listening()
        """
        ...

    def amount_hours_listening(self, hours_one_charge_level: float) -> None:
        """
        Функция, которая считает количество часов прослушивания музыки в зависимости от уровня заряда наушников

        :param hours_one_charge_level: Количество часов прослушивания от 1 процента заряда

        :raise ValueError: Если полученное количество часов превышвет количество часов при максимальном заряде, то вызываем ошибку

        :return: Полученное количество часов

        Примеры:
        >>> headphones = Headphones(7, 70)
        >>> headphones.amount_hours_listening(5)
        """
        if not isinstance(hours_one_charge_level, (int, float)):
            raise TypeError("Количество часов должно быть типа int или float")
        if hours_one_charge_level <= 0:
            raise ValueError("Количество часов должно быть положительным числом")
        ...

class Game:
    def __init__(self, storage_game: float, age: int):
        """
        Создание и подготовка к работе объекта "Видеоигра"

        :param storage_game: Занимаемая игрой память на компьютере
        :param age: Допустимый возраст для использования этой игры

        Примеры:
        >>> game = Game(30, 16)
        """
        if not isinstance(storage_game, (int, float)):
            raise TypeError("Занимаемая игрой память на компьютере должна быть типа int или float")
        if storage_game <= 0:
            raise ValueError("Занимаемая игрой память на компьютере должна быть положительным числом")
        self.storage_game = storage_game

        if not isinstance(age, int):
            raise TypeError("Допустимый возраст для использования этой игры должен быть int")
        if age < 0:
            raise ValueError("Допустимый возраст для использования этой игры не может быть отрицательным числом")
        self.age = age

    def capacity_computer(self, storage_computer: float) -> bool:
        """
        Функция, которая проверяет хватит ли память на компьютере для установления игры

        :param storage_computer: Свободная память компьютера

        :raise ValueError: Если занимаемая игрой память превышает свободную память на компьютере, то вызываем ошибку

        :return: Оставшаяся свободная память компьютера

        Примеры:
        >>> game = Game(30, 16)
        >>> game.capacity_computer(40)
        """
        if not isinstance(storage_computer, (int, float)):
            raise TypeError("Свободная память компьютера должна быть типа int или float")
        if storage_computer <= 0:
            raise ValueError("Свободная память компьютера должна быть положительным числом")
        ...

    def allowable_age(self) -> bool:
        """
        Функция, которая проверяет возможно ли играть в эту игру в зависимости от возраста

        :return: Воможность играть

        Примеры:
        >>> game = Game(30, 16)
        >>> game.allowable_age()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()
#перенос строки