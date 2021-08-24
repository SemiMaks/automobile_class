# Класс SUV представляет джип,
# и является подклассом класса Automobile.

from vehicles import Automobile


class Suv(Automobile):
    # Метод __init__ принимает аргументы для
    # изготовителя, модели, пробега, цены
    # и пассажирской вместимости.
    def __init__(self, make, model, mileage, price, pass_cap):
        # Вызвать метод __init__ надкласса и передать требуемые
        # аргументы, так же передаём self в качестве аргумента.
        Automobile.__init__(self, make, model, mileage, price)

        # Инициализируем атрибут __pass_cap.
        self.__pass_cap = pass_cap

    # Метод set_pass_cap является методом-
    # -модификатором атрибута __pass_cap

    def set_pass_cap(self, pass_cap):
        self.__pass_cap = pass_cap

    # Метод get_pass_cap является методом-
    # -получателем атрибута __pass_cap.

    def get_pass_cap(self):
        return self.__pass_cap
