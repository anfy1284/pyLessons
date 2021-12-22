# Функция для ввода чисел
def input_int(prompt, from_value = None, to_value = None, quit_string = None):
    while True:
        string = input(prompt)
        
        if string == quit_string: return None
        
        length = len(string)
        try:
            val = int(string)
        except Exception as e:
            continue        
        if (
            length == 0
            or not from_value is None and
            from_value > val
            or not to_value is None and
            to_value < val
            ):
            continue
        break      
    return val
        

# 1. Создать список и заполнить его элементами различных типов данных. 
# Реализовать скрипт проверки типа данных каждого элемента. 
# Использовать функцию type() для проверки типа. 
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_set = [1, 2.2, '3', True, [1, 2, 3], (1, 2, 3), {'a':1, 'b':2, 'c':3}, {1, 2, 3}, set, int, list]
print(type(my_set))
for v in my_set:
    print(type(v))

# 2. Для списка реализовать обмен значений соседних элементов. 
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д. 
# При нечётном количестве элементов последний сохранить на своём месте. 
# Для заполнения списка элементов нужно использовать функцию input().

# Я не хочу использовать input() для ввода списка, возьму список из предыдущей задачи

print('Before:', my_set)

new_set = my_set.copy()
for i in range(1, len(my_set), 2):
    my_set[i - 1], my_set[i] = my_set[i], my_set[i - 1]

print('After:', my_set)

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. 
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). 
# Напишите решения через list и dict. 

seasons = {'winter': 'зима', 'spring': 'весна', 'summer': 'лето' , 'fall': 'осень'}

mounth = input_int('input mounth number: ', 1, 12)

# dict
mounths_seasons_dict = {
    12: seasons['winter'], 1: seasons['winter'], 2: seasons['winter'],
    3: seasons['spring'], 4: seasons['spring'], 5: seasons['spring'],
    6: seasons['summer'], 7: seasons['summer'], 8: seasons['summer'],
    9: seasons['fall'], 10: seasons['fall'], 11: seasons['fall'],
}
print('это', mounths_seasons_dict[mounth])

# list
mounths_seasons_list = [
    seasons['winter'], seasons['winter'],
    seasons['spring'], seasons['spring'], seasons['spring'],
    seasons['summer'], seasons['summer'], seasons['summer'],
    seasons['fall'], seasons['fall'], seasons['fall'],
    seasons['winter']
]
print('это', mounths_seasons_list[mounth - 1])

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. 
# Вывести каждое слово с новой строки. Строки нужно пронумеровать. 
# Если слово длинное, выводить только первые 10 букв в слове.

my_str = input('input string: ')
words = my_str.split()
w = words.count

# Пробуем функцию enumerate
words_enum = enumerate(words)
for word in words_enum:
    print(word[0],':', word[1][:10])

# Получилось очень мило конечно, но почему-то мне кажется,
# что это будет работать чуть быстрее (могу ошибатся):
i = 0
for word in words:
    print(i,':', word[:10])
    i += 1

# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, 
# который не возрастает. У пользователя нужно запрашивать новый элемент рейтинга. 
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент 
# с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
print(my_list)
my_list.reverse()

val = 0
while True:
    val = input_int('enter new value or type \'quit\': ', None, None, 'quit')
    if val is None: break
    try:
        index = my_list.index(val)
    except Exception as e:
        index = 0
    my_list.insert(index, val)
    print(my_list[::-1])
my_list.reverse

# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. 
# Каждый кортеж хранит информацию об отдельном товаре. 
# В кортеже должно быть два элемента — номер товара и словарь с параметрами, то есть 
# характеристиками товара: 

# settings
# т.к мне лень с типами заморачиватся, все поля будут стринговые
goods_fields = ['Название', 'Цена', 'Количество', 'Ед']

# input
goods = []
record_number = 1
while True:
    good_struct = {}
    for field in goods_fields:
        val = input(str(field) + ': ')
        good_struct.update({field: val})
    goods.append((record_number, good_struct))
    next_record = input('Ввести следующий товар? (Д/Н): ').upper()[0] == 'Д'
    if not next_record : break
    record_number += 1

# calculation
stats = {}
for record in goods:
    properties = record[1]
    for property in properties.items():
        key = property[0]
        val = property[1]
        if not key in stats.keys():
            stats.update({key:[]})
        stats[key].append(val)

# output
print(goods)
print(stats)