# Задача 3. Найдите все простые несократимые дроби,
# лежащие между 0 и 1, знаменатель которых не превышает 11.
from math import gcd

d = [(i,j) for i in range(1,12) for j in range(1,12) if i<j and gcd(i,j) == 1]
print(d)
