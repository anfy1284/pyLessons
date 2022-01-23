# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. 
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве 
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroDivErr(Exception):
    txt = 'are u dumb?'

def div(a, b):
    if b == 0:
        raise ZeroDivErr
    return a / b

def safe_div(a, b):
    try:
        print(div(a, b))
    except ZeroDivErr as e:
        print(e.txt)

safe_div(10, 2)
safe_div(10, 0)

