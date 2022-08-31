# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, описывающие возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

from random import randint

# создадим список случайных целых чисел
numbers = []
for i in range(10):
    numbers.append(randint(1, 10))
print(numbers)


def ascendNums(numbers):
    ascendList = [numbers[0]]
    for i in numbers:
        if i > max(ascendList):
            ascendList.append(i)
    return ascendList


print(ascendNums(numbers))
