day=int(input("Enter a weekday number:"))
if day < 1 or day > 7:
    print("Нет такого дня")
elif day == 1:
    print("Понедельник")
elif day == 2:
    print("Вторник")
elif day == 3:
    print("Среда")
elif day == 4:
    print("Четверг")
elif day == 5:
    print("Пятница")
elif day == 6:
    print("Суббота")
elif day == 7:
    print("Воскресенье")
