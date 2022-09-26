# Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год. 
# Каждому месяцу соответствует своя строка. 
# Определите самый жаркий и самый холодный 7-дневный промежуток этого периода. Выведите его даты.

import random

def init_months_temps(months_number):
    # случайным образом определим количество дней в месяце от 30 до 31 (допущение)
    temps = [[random.randint(10, 30) for j in range(random.randint(30,31))]
             for i in range(months_number)]
    return temps

# Количество месяцев
months = 5
temps = init_months_temps(months)
print(temps)

num_month = 0
min = 0
max = 0
for i in temps:
    for j in i:
        print(j[0:7])


        
