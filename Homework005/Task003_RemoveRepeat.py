# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадаютСписок уникальных элементов [1, 4, 2, 3, 6, 7]

from random import randint

# создадим список случайных целых чисел
numbers = []
for i in range(10):
    numbers.append(randint(1, 10))
print(numbers)

def removeRepeatAndCount(numbers) :
    uniqList=[numbers[0]]
    count = 0
    for i in numbers:
        if i not in uniqList:
            uniqList.append(i)
        else:
            count += 1
    return uniqList,count

uniqList, count = removeRepeatAndCount(numbers)
print(f'{count} элементов совпадают')
print(f'Список уникальных элементов: {uniqList}')

