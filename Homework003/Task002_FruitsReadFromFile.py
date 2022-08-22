# Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.

#  cначала создадим txt файл с названиями фруктов
fruitsList = ["яблоки","арбузы","бананы","ананасы"]
with open("fruits.txt", mode="w+", encoding='utf-8') as file:
    for item in fruitsList:
        file.writelines(item+"\n")    

# теперь считаем названия фруктов из файла, убрав переводы строки
fruitsList=[]
with open("fruits.txt", mode="r", encoding='utf-8') as file:
     for line in file:
        fruitsList.append(line.rstrip())
print(fruitsList)

# выведем названия всех фруктов, начинающиеся с заданной буквы
s = 'а'
for item in fruitsList:
    if item[0] == s:
        print(item)



