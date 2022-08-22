# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.

# напишем функцию генерации последовательности Фибо в список
def getFibo(N) :
    myList = []
    myList.append(0)
    myList.append(1)
    for i in range(3,N+1) :
        myList.append(myList[i-3] + myList[i-2])
    return myList

N = 10
myList = getFibo(N)
print(myList)

# запишем получившуюся последовательность в файл
with open("Fibo.txt", "w+") as file:
    print(myList, file=file)
