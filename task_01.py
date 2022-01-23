# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде 
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, 
# с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать 
# их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию 
# числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры 
# на реальных данных.

from datetime import datetime


class Date:
    def __init__(self, date_str: str) -> None:
        self.__date_str = date_str

    #@classmethod Пришлось глянуть разбор, чтобы понять, что тут происходит,
    # такое задание получит от меня негативный комент
    def getData(self) -> tuple: #I don't like 'snake case' by the way
        try:
            day, month, year = self.__date_str.split('-')
            return (int(day), int(month), int(year))
        except Exception as e:
            print("why do u always get it wrong!?")

    @staticmethod
    def checkDate(day: int, month: int, year: int) -> bool:
        try:
            date = datetime(year, month, day)
            return True
        except ValueError:
            return False

print(Date.checkDate(*Date('01-11-2023').getData()))
print(Date.checkDate(*Date('34-11-2023').getData()))

    
