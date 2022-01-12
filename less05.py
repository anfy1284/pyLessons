# 1. Создать программно файл в текстовом формате, записать в него построчно данные, 
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

try:
    with open('task01.txt', 'w') as file_obj:
        while True:
            imput_str = input("=>")
            if not imput_str: break
            file_obj.write(imput_str)
except IOError:
    print("File write error!")
finally:
    file_obj.close() # Наверное это здесь излишне, прокомментируйте пожалуйста

# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

# Сначала 'Непрограммно' создадим файл =)

#Некоторые настройки:
NEXT_LINE_CHANCE = 0.02 #Вероятность перехода на следующую строку
GAP_CHANCE = 0.2 #Вероятность пробела
END_CHANCE = 0.001 #Вероятность окончания ввода

from functools import reduce
from random import random

try:
    with open('task02.txt', 'w') as file_obj:        
        while True:
            random_val = random()
            
            if random_val <= END_CHANCE:
                break
            elif random_val <= NEXT_LINE_CHANCE:
                file_obj.write('\n')
            elif random_val <= GAP_CHANCE:
                file_obj.write(' ')
            else:
                #Не будем замороачиваться с буквами, будем заполнять знаком '#'
                file_obj.write('#')            
except IOError:
    print("File write error!")
finally:
    file_obj.close()

# Теперь почитаем
try:
    with open('task02.txt', 'r') as file_obj:
        lines = file_obj.readlines()
        print(f'Trere are {len(lines)} lines')
        n = 1
        for line_in in lines:
            print(f'Line #{n} has {len(line_in.split())} words')
            n += 1
except IOError:
    print("File read error!")
finally:
    file_obj.close()

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и 
# величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., 
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

# Ну ОК, создадим по приколу генератор фамилий

from random import randint
from itertools import cycle

SYLLABLES_LETTERS_COUNT = 2 #Количество букв в слоге
SYLLABLE_EXTRA_LETTER_CHANCE = 0.01 #Вероятность +1 буквы в слоге
SYLLABLES_MAX_COUNT = 3 #Максимальное количество слогов в фамилии, не считая окончания
#FEMALE_CHANCE = 0.5  #Вероятность женского окончания
FIRST_VOWEL_LETTER_CHANCE = 0.6 #Вероятность, что фамилия начинается с гласной

#Списки букв в прорядке частотности, и некоторые убраны
vowels = ['о', 'е', 'а', 'и', 'у', 'я']
consonants = ['н', 'т', 'с', 'р', 'в', 'л', 'к', 'м', 'д', 'п', 'г', 'з', 'б', 'ч', 'х', 'ж', 'ш']

endings = ['ов', 'ова', 'ев', 'ева', 'ин', 'ина', 'ич']

def get_random_item(items):
    """Функция выбирает случайный элемент из входящего списка,
    вероятность выбора элемента тем выше, чем ближе он к началу списка"""
    chance = 1 / len(items)
    for item in cycle(items):
        random_val = random()
        if random_val <= chance:
            return item


def syllable_letters_count(is_extra_letter_necessarily):
    result = SYLLABLES_LETTERS_COUNT
    if is_extra_letter_necessarily:
        result += 1
    else:
        random_val = random()
        if random_val <= SYLLABLE_EXTRA_LETTER_CHANCE:
            result += 1
    return result

def random_russian_last_name():
    result = ''    

    syll_count = 0

    #Первый слог - возможно с гласной
    random_val = random()
    if random_val <= FIRST_VOWEL_LETTER_CHANCE:
        #result += vowels[randint(0, len(vowels) - 1)]
        result += get_random_item(vowels)
        syll_count += 1

    syll_max_count = randint(1, SYLLABLES_MAX_COUNT - 1)
    if syll_count == syll_max_count:
        syll_max_count += 1

    for syll in range(syll_count, syll_max_count):
        letters_max_count = syllable_letters_count(syll == syll_max_count - 1)
        letters_count = 0
        for letter_list in cycle([consonants, vowels]):
            letters_count += 1
            #result += letter_list[randint(0, len(letter_list) - 1)]
            result += get_random_item(letter_list)
            if letters_count >= letters_max_count: break

    #Последний слог - окончание
    result += endings[randint(0, len(endings) - 1)]
    
    return result.capitalize()

#Генерируем файлик

EMPLOEE_NUMBER = 1000 #Количество сотрудников
MAX_SALARY = 500000 #Максимальная з/п

try:
    with open('task03.txt', 'w', encoding='utf-8') as file_obj:
        for i in range(1, EMPLOEE_NUMBER):
            file_obj.write(f'{random_russian_last_name()} {(random() * MAX_SALARY):.2f}\n')
except IOError:
    print("File write error!")
finally:
    file_obj.close()

#Собственно задача:

OUTPUT_SALARY = 20000

try:
    with open('task03.txt', 'r', encoding='utf-8') as file_obj:
        summ = 0
        lines = file_obj.readlines()
        print('Here\'s the loosers:')
        for line_in in lines:
            last_name, salary_str = line_in.split()
            salary = float(salary_str)
            summ += salary
            if salary < OUTPUT_SALARY:
                print(f'{last_name}: {salary:.2f}')
        print(f'And average salary is {(summ / len(lines)):.2f}')                
except IOError:
    print("File read error!")
finally:
    file_obj.close()


# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
# При этом английские числительные должны заменяться на русские. 
# Новый блок строк должен записываться в новый текстовый файл.

trans_dict = {'One': 'Ван', 'Two': 'Ту', 'Three': 'Три', 'Four': 'Фо'}

def trans(word):
    found = trans_dict.get(word)
    if found:
        return found
    else:
        return word

try:
    with open('task04_in.txt', 'r', encoding='utf-8') as file_obj_in, open('task04_out.txt', 'w', encoding='utf-8') as file_obj_out:
        lines = file_obj_in.readlines()
        for line_in in lines:
            file_obj_out.write(f'{" ".join([trans(word) for word in line_in.split()])}\n')
except IOError:
    print("File read error!")
finally:
    file_obj_in.close()
    file_obj_out.close()


# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

NUMBERS_NUMBER = 100 #Количество чисел
MAX_NUMBER = 1000 #Максимальное число

try:
    with open('task05.txt', 'w') as file_obj:
        file_obj.write(" ".join([str(round(random() * MAX_NUMBER, 2)) for i in range(NUMBERS_NUMBER)]))
    with open('task05.txt', 'r') as file_obj:
        print(f'Сумма = {reduce(lambda x, y: x + y, [float(item) for item in file_obj.read().split()]):.2f}')
except IOError:
    print("File read/write error!")
finally:
    file_obj.close()

# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает 
# учебный предмет и наличие лекционных, практических и лабораторных занятий по этому 
# предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —

# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

try:
    with open('task06.txt', 'r', encoding='utf-8') as file_obj:
        lines = file_obj.readlines()
        result_dict = {}
        for line in lines:
            subject, hours_str = line.split(':')
            hours_summ = 0
            for sub_hours_str in hours_str.split():
                summ = 0
                for c in sub_hours_str:
                    if c.isdigit(): summ = summ * 10 + int(c)
                hours_summ += summ
            result_dict.update({subject: hours_summ})

        print(result_dict)
        
except IOError:
    print("File read error!")
finally:
    file_obj.close()

# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: 
# название, форма собственности, выручка, издержки.

# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, 
# а также словарь со средней прибылью. Если фирма получила убытки, 
# также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

# Подсказка: использовать менеджеры контекста.

import json

try:
    with open('task07_in.txt', 'r', encoding='utf-8') as file_obj:
        lines = file_obj.readlines()
        result_dict = {}
        summ = 0
        count = 0
        for line in lines:
            firm, firm_type, revenue_str, expenses_str = line.split()
            profit = float(revenue_str) - float(expenses_str)
            result_dict.update({firm: profit})
            if profit > 0:
                summ += profit
                count += 1
        
        result_list = [result_dict, {"average_profit": summ / count if count != 0 else 0}]
        print(result_list)

    with open('task07_out.txt', 'w') as file_obj:
        json.dump(result_list, file_obj)

except IOError:
    print("File read/write error!")
finally:
    file_obj.close()
