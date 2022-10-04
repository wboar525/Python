#Задача 2. Имеются данные о площади и стоимости 15 домов.
#Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000 рублей.
#Предоставьте ему графические данные о стоимость квадратного метра каждого дома и 
#список подходящих ему домов, отсортированных по площади.
#Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров, цены от 3 до 20 млн.

import random
import matplotlib.pyplot as mat

data = [[random.randint(100,300),random.randint(3000000,20000000)] for x in range(15)]
sq = []
for i in data:
	sq.append(int(i[1])/int(i[0]))
mat.grid(which='major')
mat.xlabel("Номер дома")
mat.title("Стоимость кв.м.")
mat.plot(sq)
mat.plot(list(50000 for i in range(len(data))))
mat.show()

fit=[]
for i in range(len(data)):
	if sq[i]<50000:
		fit.append(data[i])
fit.sort()
for i in fit:
	print(f'Площадь дома: {i[0]} кв.м., стоимость: {i[1]}')
