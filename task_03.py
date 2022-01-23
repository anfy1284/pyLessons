# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на 
# наличие только чисел. Проверить работу исключения на реальном примере. Запрашивать у
# пользователя данные и заполнять список необходимо только числами. Класс-исключение 
# должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь 
# сам не остановит работу скрипта, введя, например, команду «stop». При этом скрипт завершается, 
# сформированный список с числами выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. 
# Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента. 
# Вносить его в список, только если введено число. Класс-исключение должен не позволить 
# пользователю ввести текст (не число) и отобразить соответствующее сообщение. 
# При этом работа скрипта не должна завершаться.

class MyExeption(Exception):
    pass

def number(str):
    try:
        return float(str)
    except Exception as e:
        raise MyExeption

def inputNumber(prompt, stopWord = 'stop'):
    while True:
        string = input(prompt)
        if string.lower() == stopWord.lower():
            return False, None
        length = len(string)
        if length == 0: continue
        try:
            return True, number(string)
        except MyExeption:
            print('That\'s not a number! try again!')
            continue

def imputList():
    list = []
    print('input some numbers, and then print \'stop\'')
    isContinue = True
    while True:
        isContinue, newItem = inputNumber(' => ')
        if isContinue:
            list.append(newItem)
        else:
            break
    return list

print(imputList())
