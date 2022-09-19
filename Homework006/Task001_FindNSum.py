# Дано натуральное число N. Найдите значение выражения:N + NN + NNN. N может быть любой длины.
# N = 132: 132 + 132132 + 132132132 = 132264396
str=input()
num=[]
str1 = str
for i in range(0,3):
    num.append(int(str))
    str += str1
print(num)
print(sum(num))
