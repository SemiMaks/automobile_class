# Класс Truck представляет пикап,
# и является подклассом класса Automobile.

from vehicles import Automobile


class Truck(Automobile):
    # Метод __init__ принимает аргументы для
    # изготовителя, модели, пробега, цены и типа привода.

    def __init__(self, make, model, mileage, price, drive_type):
        # Вызвать метод __init__ надкласса и передать
        # требуемые аргументы.
        # Так же передаем self в качестве аргумента.
        Automobile.__init__(self, make, model, mileage, price)

        # Инициализировать атрибут __drive_type.
        self.__drive_type = drive_type

    # метод set_drive_type является методом-модификатором
    # атрибута __drive_type.

    def set_drive_type(self, drive_type):
        self.__drive_type = drive_type

    # Метод get_drive_type является методом-
    # -получателем атрибута __drive_type.

    def get_drive_type(self):
        return self.__drive_type
