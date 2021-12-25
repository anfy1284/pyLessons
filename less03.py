# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) 
# и выполняющую их деление. Числа запрашивать у пользователя, 
# предусмотреть обработку ситуации деления на ноль.

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        pass
        # TODO обработка ситуации деленая на ноль

# 2. Выполнить функцию, которая принимает несколько параметров, 
# описывающих данные пользователя: имя, фамилия, год рождения, 
# город проживания, email, телефон. Функция должна принимать 
# параметры как именованные аргументы. Осуществить вывод данных 
# о пользователе одной строкой.

def user_info_out(**kwargs):
    return kwargs

# 3. Реализовать функцию my_func(), которая принимает три позиционных 
# аргумента и возвращает сумму наибольших двух аргументов.

def my_func(arg_1, arg_2, arg_3):
    return arg_1 + arg_2 + arg_3 - min(arg_1, arg_2, arg_3)

# 4. Программа принимает действительное положительное число x и целое 
# отрицательное число y. Выполните возведение числа x в степень y. 
# Задание реализуйте в виде функции my_func(x, y). При решении задания 
# нужно обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. 
# Первый — возведение в степень с помощью оператора **. 
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x, y):
    val = x
    for i in range(y-1):
        val *= x 
    return val

# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. 
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить 
# ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь введённых 
# чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится 
# специальный символ, выполнение программы завершается. Если специальный символ 
# введён после нескольких чисел, то вначале нужно добавить сумму этих чисел к 
# полученной ранее сумме и после этого завершить программу.

def input_list():
    return input(' => ').split()

def sum_str_list(str_list, stop_word):
    sum = 0
    errors = []
    is_end = False
    for item in str_list:
        try:
            sum += float(item)
        except Exception as e:
            if str(item).lower() == stop_word: #преобразуем в str на всякий случай от греха подальше :) для отказоустойчивости
                is_end = True
                break
            else:
                errors.append(str(item))
    return sum, errors, is_end #Офигенно, что так можно! не ну конечно в других языках ничего не мешает структуру сгенерировать и вернуть но всё равно - круто!
    
print('Input so many numbers as you want or know, and when you get tired, write \'banana\', it\'s gonna be our secret stop-word. And maybe I\'ll count your numbers.')

is_end = False
current_sum = 0
while not is_end: # а вот то что нельзя написать "!is_end" это конечно минус им в карму
    list = input_list()
    sum, errors, is_end = sum_str_list(list, 'banana')
    current_sum += sum
    print('your sum now is', current_sum)
    if errors:
        print('I don\'t know what did you mean, wrote this:', errors, 'but these are definitely not numbers and I didn\'t count them')

# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских 
# букв и возвращающую их же, но с прописной первой буквой. Например, 
# print(int_func(‘text’)) -> Text.

def int_func(*args):
    return list(map(lambda s: s.capitalize(), args))

# 7. Продолжить работу над заданием. В программу должна попадать строка из слов, 
# разделённых пробелом. Каждое слово состоит из латинских букв в нижнем регистре. 
# Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной 
# буквы. Используйте написанную ранее функцию int_func().

print(int_func(*(input(' ==> ').split())))