# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. 
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название. 
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: 
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), 
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: 
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу 
# декоратора @property.

from abc import abstractproperty


class Clothes:    
    def __init__(self, name) -> None:
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    @abstractproperty
    def consumption(self):
        """consumption"""


class Coat(Clothes):
    def __init__(self, name, v) -> None:
        self.__v = v
        super().__init__(name)
    
    @property
    def consumption(self):
        return (self.__v / 6.5 + 0.5)


class Suit(Clothes):
    def __init__(self, name, h) -> None:
        self.__h = h
        super().__init__(name)
    
    @property
    def consumption(self):
        return (2 * self.__h + 0.3)

my_coat = Coat('coat 1', 15)
my_suit = Coat('suit 1', 3)

print(my_coat.consumption)
print(my_suit.consumption)
