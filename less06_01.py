# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.

from itertools import cycle
from time import sleep

class TrafficLight:
    
    class TrafficLightColor:
        def __init__(self, color, time):
            self.color = color
            self.time = time

    colors = [TrafficLightColor("Red", 7), 
            TrafficLightColor("Green", 2),
            TrafficLightColor("Blue", 5)]

    def __init__(self):
        self.__color = self.colors[0]
        self.running()
    
    def running(self):
        this = self
        my_cycle = cycle(this.colors)
        for color in my_cycle:
            if color == this.__color:
                print(color.color)
                sleep(color.time)
                this.__color = next(my_cycle)

traffic_light = TrafficLight()