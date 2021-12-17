def input_int(prompt):
    while True:
        string = input(prompt)
        length = len(string)
        if length == 0: continue
        try:
            return int(string)
        except:
            continue

#1.
# Поработайте с переменными, создайте несколько, выведите на экран, запросите
# у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

int_val = 1
str_val = '2'

a = input('please input a: ')
b = input('please input b: ')
print('thanks!, you wrote a =', a, 'and b =', b, ' I proud of u!')

#2.
# Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

secs = input_int('how many seconds?: ')
mins = secs // 60
secs = secs % 60
hours = mins // 60
mins = mins % 60
print(f'{hours}:{mins}:{secs}')

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

REPS = 4
n = input_int('n = ')

summ = 0
for i in range(1, REPS):
    sub_summ = 0
    for j in range(i, REPS):
        sub_summ = sub_summ * 10 + n
    summ += sub_summ

print('summ =', summ)

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

string = str(input_int('input int: '))

max = int(string[0])
n = 1
while n < len(string) and max < 9:
    current = int(string[n])
    if max < current : max = current
    n += 1

print('max is ', max)

# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите,
# с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчете на одного сотрудника.

profit = input_int('profit = ')
loss = input_int('profit = ')

margin = profit - loss
efficiency = 0
is_good = False

if margin > 0:
    efficiency = profit / margin
    print('looks like it\'s allright! efficiency = ', efficiency)
    is_good = True
else:
    print('something went wrong!')

if is_good:
    staff_number = input_int('staff number = ')
    if staff_number > 0 :
        margin_per_person = margin / staff_number
        print(f'margin per person = {margin_per_person:.2f}')


# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a
# километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить
# не менее b километров. Программа должна принимать значения параметров a и b и
# выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
#
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

INC = 1.1

a = input_int('a = ')
b = input_int('b = ')

print('Результат:')

distance = a
day = 1
while True:
    print(f'{day}-й день: {distance:.2f}')
    if distance >= b: break
    distance *= INC
    day += 1 

print()
print(f'Результат: на {day}-й день спортсмен достиг результата — не менее {b} км.')