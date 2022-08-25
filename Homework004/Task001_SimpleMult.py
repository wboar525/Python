# Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5

sMult = [2, 3, 5, 7, 11, 13, 17]

num = int(input('Введите число для разложения на простые множители: '))


def findLowestSM(num, sm):
    for i in sm:
        if num % i == 0:
            return i
    return 0


myList = []
res = num
while (res > 1):
    sm = findLowestSM(res, sMult)
    if sm != 0:
        myList.append(sm)
        res = res / sm
    else:
        break

print(myList)
