# Задача 1. В каждой группе учится от 20 до 30 студентов.
# По итогам экзамена все оценки заносятся в таблицу. Каждой группе отведена своя строка.
# Определите группу с наилучшим средним баллом.

import random

def init_group_marks(groups):
    # случайным образом определим количество студентов в группе
    marks = [[random.randint(2, 5) for j in range(random.randint(20,30))]
             for i in range(groups)]
    return marks


# Зададим количество групп
groups = 5
marks = init_group_marks(5)
print(marks)
max = 0
num = 1
for i in marks:
    mean = 0
    for j in i:
        mean += j
    mean /= len(i)
    if mean > max:
        max = mean
        num_max = num
    print(f'Группа №{num}, средний балл {mean}')
    num += 1
print("Наивысший балл в группе номер", num_max)
