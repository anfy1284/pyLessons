# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). 
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. 
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

from typing_extensions import ParamSpec


class Stationery:
    title = ''
    def draw(self):
        print("Запуск отрисовки")

class Pen:
    def draw(self):
        print('уникальное сообщение класса Pen')

class Pencil:
    def draw(self):
        print('уникальное сообщение класса Pencil')

class Handle:
    def draw(self):
        print('уникальное сообщение класса Handle')

Stationery().draw()
Pen().draw()
Pencil().draw()
Handle().draw()

