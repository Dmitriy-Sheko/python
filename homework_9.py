#1
from time import sleep
from itertools import cycle

class TrafficLight:
    def __init__(self):
        self.__color = (('Красный', 7), ('Жёлтый', 2), ('Зелёный', 5))
    def running(self):
        for color, sec in cycle(self.__color):
            print(color, '(осталось {} секунд)'.format(sec))
            sleep(sec)
traffic_light = TrafficLight()
traffic_light.running()


#2
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def all_mass(self):
        mass = self._length * self._width * 25 * 5 / 1000
        return mass

all_road = Road(20, 5000)
print('Асфальта потребуется', all_road.all_mass(), 'т')


#3
class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']
class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname} {self.position}'
    def get_total_income(self):
        return self._income_wage + self._income_bonus

pos = Position('Билл', 'Гейтс', 'директор', {"wage": 1, "bonus": 99999999999999})
print(pos.get_full_name())
print(pos.get_total_income())


#4
class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехла.'

    def stop(self):
        return f'\n{self.name} остановилась.'

    def turn(self, direction):
        return f'\n{self.name} повернула {direction}'

    def show_speed(self):
        return f'\nВаша скорость: {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nВы превысили скорость.Ваша скорость: {self.speed}'
        else:
            return f'Speed of {self.name} is normal'

class SportCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nВы превысили скорость.Ваша скорость: {self.speed}'
        else:
            return f'Speed of {self.name} is normal'

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nВы превысили скорость.Ваша скорость: {self.speed}'
        else:
            return f'Скорость {self.name} допустимая'

class PoliceCar(Car):
    pass

town = TownCar('Городская машина', 70, 'черная', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('налево'), town.turn('направо'), town.stop())

sport = SportCar('Спортивная машина', 170, 'красная', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('налево'), sport.stop())

work = WorkCar('Рабочая машина', 30, 'зеленая', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('нараво'), work.stop())

police = PoliceCar('Полицейская машина', 100, 'синяя', True)
print('4:\n' + police.go(), police.show_speed(), police.turn('направо'), police.stop())


#5
class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Ручка рисует')

class Pencil(Stationery):
    def draw(self):
        print('Карандаш рисует')

class Handle(Stationery):
    def draw(self):
        print('Маркер рисует')

pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')

pen.draw()
pencil.draw()
handle.draw()