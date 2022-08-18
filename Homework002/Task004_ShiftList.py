# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

# создадим список из num числа элементов
num = 3
list1 = []
for i in range(-num,num+1):
    list1.append(i)
print(list1)

# напишем функцию циклического сдвига на steps элементов вправо
def shift(list1, steps) :
    length = len(list1)
    for i in range(1,steps+1):
        el = list1[length-1]
        list1.pop(length-1)
        list1.insert(0,el)    
    return list1

# сдвинем список вправо и выведем результат
list2 = shift(list1,2)
print(list2)
