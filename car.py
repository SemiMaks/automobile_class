from vehicles import Automobile


# Класс Car представляет легковой автомобиль.
# Он является подклассом класса Automobile.

class Car(Automobile):
    # Метод __init__ принимает аргумегты для фирмы-
    # -изготовителя, модели, пробега, цены и количества дверей.

    def __init__(self, make, model, mileage, price, doors):
        # Вызвать метод __init__ надкласса и передать
        # требуемые элементы. Тут так же
        # передаём self в качестве аргумента.

        Automobile.__init__(self, make, model, mileage, price)
        # Инициализировать атрибут __doors.
        self.__doors = doors

    # Метод set_doors является методом-
    # -получателем атрибута __doors

    def set_doors(self, doors):
        self.__doors = doors

    # Метод get_doors является методом-
    # -получателем атрибута __doors

    def get_doors(self):
        return self.__doors
