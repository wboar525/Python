# Задача 2. В первой строке файла находится информация об ассортименте мороженного, во второй - информация о том, какое мороженное есть на складе. Выведите названия того товара, который закончился.
# 1. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2. «Сливочное», «Вафелька», «Сладкоежка»
# Закончилось: «Бурёнка»

#  cначала создадим csv файл с ассортиментом и наличием
import csv

iceAssort = ["Сливочное", "Буренка", "Вафелька", "Сладкоежка"]
iceInStock = ["Сливочное", "Вафелька", "Сладкоежка"]

with open('icecream.csv', 'w+', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"',
                        quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(iceAssort)
    writer.writerow(iceInStock)

# теперь считаем названия мороженого из файла
with open('icecream.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=',')
    iceAssort = reader.__next__()
    iceInStock = reader.__next__()

print(iceAssort)
print(iceInStock)

res = (set(iceAssort) ^ set(iceInStock))
print(f'Закончилось: {res}')
