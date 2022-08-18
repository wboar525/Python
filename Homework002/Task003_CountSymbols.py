# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 3(2 на самом деле)

str1=input('Введите первую строку: ')
str2=input('Введите вторую строку: ')
list1=list(str1)
list2=list(str2)
for s1 in list1:
    count=0
    for s2 in list2:
        if s1 == s2:
            count += 1
    print(s1,'->',count)