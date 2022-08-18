from math import sqrt

xa = float(input("Введите координату х точки А: "))
ya = float(input("Введите координату y точки А: "))
xb = float(input("Введите координату х точки B: "))
yb = float(input("Введите координату y точки B: "))
dist = (sqrt((xa-xb)**2 + (ya-yb)**2))
print("Расстояние = ",dist)