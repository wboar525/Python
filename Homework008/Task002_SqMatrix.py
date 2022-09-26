# Задача 2. Дана квадратная матрица, заполненная случайными числами. 
# Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.

import random

# инициализируем квадратную матрицу случайными числами
def init_matrix(n):
    matrix = [[random.randint(1, 10) for j in range(n)] for i in range(n)]
    return matrix

size = 5
matrix = init_matrix(size)
print(matrix)

# посчитаем сумму главной диагонали
diag_sum = 0
for i in range(0,size):
    diag_sum += matrix[i][i]
print(f'Сумма элементов диагонали равна {diag_sum}')

# посчитаем суммы элементов строк
num_row = 1
for i in matrix:
    sum = 0
    for j in i:
        sum += j
    if sum > diag_sum:
        print(f'Cумма элементов строки {num_row} равна {sum} и больше суммы элементов диагонали')
    num_row += 1

