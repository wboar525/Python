# Задача 4*. Создайте игру в крестики-нолики.

from random import randint


def initPG(n, m):
    matrix = [[0 for j in range(m)] for i in range(n)]
    return matrix

def printPG(matrix):
    for row in matrix:
        for x in row:
            if x == 0:
                print('*', end=" ")
            elif x == 1:
                print('X', end=" ")
            elif x == 2:
                print('0', end=" ")
        print()

def makeStep(matrix, n, m, type):
    name = 'Крестики'
    if type == 2:
        name = 'Нолики'
    x = int(input(f'{name}: введите ваш ход по горизонтали от 1 до {n}: '))
    y = int(input(f'{name}: введите ваш ход по вертикали от 1 до {m}: '))

    if x > m or y > n:
        return False

    x = x - 1
    y = y - 1
    if matrix[y][x] == 0:
        matrix[y][x] = type
    else:
        return False
    return True

# Функция проверки условий выигрыша
def checkWinCondition(matrix, type):
    countD = 0  # основная диагональ
    countBD = 0  # побочная диагональ

    for i in range(len(matrix)):
        if matrix[i][i] == type:
            countD += 1
        if matrix[i][len(matrix)-1-i] == type:
            countBD += 1

        countH = 0  # cчетчик горизонтальных значений
        for j in range(len(matrix[i])):
            if matrix[i][j] == type:
                countH += 1
        if countH == len(matrix):
            return True, type

    if countD == len(matrix) or countBD == len(matrix):
        return True, type

    # Для проверки выигрыша по вертикали, повернем исходную матрицу на 90 градусов и прогоним новую матрицу по строкам
    newMatrix = [[matrix[j][i] for j in range(
        len(matrix))] for i in range(len(matrix[0])-1, -1, -1)]
    for i in range(len(newMatrix)):
        countH = 0
        for j in range(len(newMatrix[i])):
            if newMatrix[i][j] == type:
                countH += 1
        if countH == len(newMatrix):
            return True, type

    return False, type

n = 3
m = 3
print(f'Игра "Крестики-нолики", поле {n} X {m}')
playGround = initPG(n, m)
printPG(playGround)

end = False
type = 2
while end == False:
    if type == 1:
        type = 2
    else:
        type = 1
    while makeStep(playGround, n, m, type) == False:
        print('Клетка занята или введены неправильные координаты')
    printPG(playGround)
    end, type = checkWinCondition(playGround, type)

if type == 1:
    print("Крестики выиграли!")
if type == 2:
    print("Нолики выиграли!")
print("Игра окончена.")
