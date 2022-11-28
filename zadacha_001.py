# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. 
# Учтите, что числа могут быть отрицательными

# Пример:

# 67.82 -> 23
# (-0.56) -> 11

chislo = float(input('введите вещетвенное число '))
print(chislo)

m_chislo = abs(chislo)
summa = 0

while m_chislo > 0:
    a = chislo % 10
    summa = summa + a 
    m_chislo = m_chislo // 10 
print ('сумма', summa)

