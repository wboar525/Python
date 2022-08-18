# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

num=int(input('Input your number: '))
myList = []
for i in range(1,num+1) :
    fact = 1
    for j in range(1,i+1) :
        fact = fact*j
    myList.append(fact)
print(myList)