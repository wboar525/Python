# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8

from random import randint

numbers = []
for i in range(10):
    numbers.append(randint(1, 10))
print(numbers)

print(list(filter(lambda x: x > 5, numbers)))
