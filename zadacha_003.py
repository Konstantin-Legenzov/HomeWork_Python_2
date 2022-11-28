# 3 - Дан массив размера N.
# После каждого отрицательного элемента массива вставьте элемент с нулевым значением.

# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

import random

list_1 = []
number = int(input('Введите число '))

for i in range(0, number):
    a = random.randint(-10, 10)
    list_1.append(a)
print(list_1)


def _put_zero_(x):
    i = 0
    if list_1[i] < 0:
        list_1.insert(i + 1, 0)
        i = i + 1
    else:
        i = i +1
    return 

print(_put_zero_(list_1))

