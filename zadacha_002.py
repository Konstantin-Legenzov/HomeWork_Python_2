# 2 - Напишите программу, которая принимает на вход число N и 
# выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] #(1, 1*2, 1*2*3, 1*2*3*4)

import math

chislo = int(input('Введите число: '))
r = range(0, chislo)

for i in r:
    print(i+1)

spisok = list(range(1, i+2))
print(spisok)

def mult(x):
    count = 1
    for j in x:
        count*= j
    return count

print(mult(spisok))


spisok[-1] = mult(spisok)

print(spisok)