# Задача 4*. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# 5x^2 + 3x
# 3x^2 + x + 8
# 8x^2 + 4x + 8

import csv
import re

# Создадим два файла с многочленами
poly1 = ["5x^2", "+", "3x"]
poly2 = ["3x^2", "+", "x", "+", "8"]

with open('poly1.csv', 'w+', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
    writer.writerow(poly1)

with open('poly2.csv', 'w+', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
    writer.writerow(poly2)

# теперь считаем многочлены из файлов
with open('poly1.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=',')
    poly1 = reader.__next__()

with open('poly2.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=',')
    poly2 = reader.__next__()

# напишем функцию определения степени и множителя каждого элемента многочлена


def findOrderAndRatio(poly):
    # используем regexp для нахождения чисел по шаблону, итератор чтобы получить список чисел а не строк
    digits = [int(s) for s in re.findall(r'[-+]?\d+', poly)]
    order = 0
    ratio = 0
    if len(digits) > 1:
        return digits[1], digits[0]

    isdegree = '^' in poly  # есть ли в строке степень
    isx = 'x' in poly  # есть ли в строке х
    if len(digits) == 1:
        if isdegree:
            return digits[0], 1
        elif isx:
            return 1, digits[0]
        else:
            return 0, digits[0]
    if len(digits) == 0:
        if isx:
            return 1, 1
        else:
            return 0, 0
    return order, ratio


# построим получившийся многочлен в текстовом формате
def buildNewPoly(dict):
    newPoly = []
    for order, ratio in dict.items():
        text = ''
        # если многочлен не первый - добавим его знак
        index = list(dict).index(order)
        if (index > 0):
            if (ratio >= 0):
                newPoly.append('+')
            else:
                newPoly.append('-')

        if abs(ratio) > 1:
            text += str(abs(ratio))
        if order > 0:
            text += 'x'
        if order > 1:
            text += "^"
            text += str(order)
        newPoly.append(text)
    return newPoly


# переведем 1-й файл с многочленами в формат словаря, где ключ=степень:значение=множитель
dict = {}
for item in poly1:
    if (item != '+'):
        order, ratio = findOrderAndRatio(item)
        dict[order] = ratio

# прибавим многочлены из 2-го файла при наличии совпадений, иначе - добавим их в словарь
for item in poly2:
    if (item != '+'):
        order, ratio = findOrderAndRatio(item)
        if (order in dict):
            dict[order] = dict[order] + ratio
        else:
            dict[order] = ratio

text = buildNewPoly(dict)
print(text)

with open('newpoly.csv', 'w+', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
    writer.writerow(text)
