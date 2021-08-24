# Эта программа демонстрирует класс Car.

from car import Car
from truck import Truck
from SUV import Suv


def main():
    print('Наличие поддержанных автомобилей на складе: ')

    # Создать объект на основе класса Car.
    # Легковое авто: 2007 Audi с 12500 миль пробега,
    # ценой $21500.00 и с 4 дверьми.
    used_car = Car('Audi', 2007, 12500, 21500.0, 4)

    # Создать объект на основе класса Truck.
    # Пикап: 2010 Пикап с 15000 миль пробега,
    # ценой $25600.00 и с наличием привода.
    used_truck = Truck('Пикап', 2010, 15000, 25600, 'Да')

    # Создать объект на основе класса SAU.
    # Volvo 2015 с 17000 миль пробега,
    # ценой $29000.00 и с 5ю дверьми.
    used_suv = Suv('Volvo', 2015, 17000, 29000, '5')

    # Показать данные легкового автомобиля.
    print('-' * 35)
    print('Изготовитель: ', used_car.get_make())
    print('Модель: ', used_car.get_model())
    print('Пробег: ', used_car.get_mileage())
    print('Цена: ', used_car.get_price())
    print('Количество дверей: ', used_car.get_doors())

    # Показать данные пикапа.
    print('-' * 35)
    print('Изготовитель: ', used_truck.get_make())
    print('Модель: ', used_truck.get_model())
    print('Пробег: ', used_truck.get_mileage())
    print('Цена: ', used_truck.get_price())
    print('Наличие полного привода: ', used_truck.get_drive_type())

    # Показать данные SUV.
    print('-' * 35)
    print('Изготовитель: ', used_suv.get_make())
    print('Модель: ', used_suv.get_model())
    print('Пробег: ', used_suv.get_mileage())
    print('Цена: ', used_suv.get_price())
    print('Количество дверей: ', used_suv.get_pass_cap())


main()
