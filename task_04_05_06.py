# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
# А также класс «Оргтехника», который будет базовым для классов-наследников. 
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
# В базовом классе определите параметры, общие для приведённых типов. 
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём 
# оргтехники на склад и передачу в определённое подразделение компании. Для хранения данных о 
# наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую 
# подходящую структуру (например, словарь).

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых 
# пользователем данных. Например, для указания количества принтеров, отправленных на склад, 
# нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, 
# изученных на уроках по ООП.


import re
from tkinter import N


class WareHouse:
    def __init__(self) -> None:
        self.__balance = {}

    def get_in(self, item, count, isGetOut = False):
        if type(count) != int and type(count) != float:
            raise NameError('Число должно быть числом, а если число не число, то ничто не число!')

        if isGetOut: count = - count

        found = self.__balance.get(item)
        if found:
            self.__balance[item] += count
        else:
            self.__balance.update({item: count})

    def get_out(self, item, count):
        self.get_in(item, count, True)

    def show_storage(self):
        s = '{\n'
        for item in self.__balance:
            s += f' {item} : {self.__balance[item]}\n'
        s += '}'
        return s 
    
    @staticmethod
    def move(ware_house_from, ware_house_to, item, count):
        try: #Типа транцакция
            got_out = False
            ware_house_from.get_out(item, count)
            got_out = True
            ware_house_to.get_in(item, count)
        except Exception as e:
            print(e)
        finally:
            #Если что-то пошло не так, постараемся сделать как было
            if got_out: ware_house_from.get_in(item, count)

class OfficeEquipment:
    def __init__(self, name, common_property) -> None:
        self.__name = name
        self.__common_property = common_property
    
    @property
    def common_property(self):
        return self.__common_property

    @common_property.setter
    def common_property(self, value):
        self.__common_property = value

    def __str__(self):
        return self.__name

class Printer(OfficeEquipment):
    def __init__(self, name, common_property, self_property) -> None:
        super().__init__(name, common_property)
        self.self_property = self_property

class Scaner(OfficeEquipment):
    def __init__(self, name, common_property, self_property) -> None:
        super().__init__(name, common_property)
        self.self_property = self_property

class PortalGun(OfficeEquipment):
    def __init__(self, name, common_property, self_property) -> None:
        super().__init__(name, common_property)
        self.self_property = self_property

prn = Printer('Printer 1', 'qwe','rer')
print(prn)
bfg = PortalGun('BFG 9000', 'erth','afg')

wh1 = WareHouse()
wh2 = WareHouse()

wh2.get_in(bfg, 3)
print(wh2.show_storage())

wh1.get_in(prn, 3)
print(wh1.show_storage())

wh1.get_in(prn, 2)
print(wh1.show_storage())

wh1.get_out(prn, 1)
print(wh1.show_storage())

WareHouse.move(wh1, wh2, prn, 1)
print(wh1.show_storage())
print(wh2.show_storage())

WareHouse.move(wh1, wh2, prn, "1")
print(wh1.show_storage())
print(wh2.show_storage())
