# Задача 2. Задан массив из случайных цифр на 15 элементов. 
# На вход подаётся трёхзначное натуральное число. 
# Напишите программу, которая определяет, 
# есть в массиве последовательность из трёх элементов, 
# совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет
import random

my_list = [random.randint(0,9) for i in range(0,15)]
print(my_list)

num = input("Введите число: ")
str = "".join(map(str,my_list))
if (num in str):
    print("да")
else:
    print("нет")