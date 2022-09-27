import telebot
import requests
import numexpr
import random

num = random.randint(0,1000)
count = 0

bot = telebot.TeleBot(
    "", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(content_types=["text", "sticker"])
def function_name(message):
    global num, count
    # bot.reply_to(message, "Сообщение сохранено")
    text = message.text
    # print(message)
    if 'привет' in text.lower():
        bot.reply_to(message, f'Привет, {message.from_user.first_name}!')
    elif 'погода' in text.lower():
        weather = requests.get('https://wttr.in/?0T')
        bot.reply_to(message, weather.text)
    elif 'кот' in text.lower():
        photo = open('c:/cat.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo) 
    elif 'выражение' in text.lower(): # Задача №1
        expr = text.split()[1]
        res = numexpr.evaluate(expr)
        bot.reply_to(message, f'Выражение {expr} равно {res}')
    elif text.isdecimal(): # Задача №2, игра начинается просто при вводе любого десятичного числа
        ent_num = int(text)
        count += 1
        if ent_num > num:
            bot.reply_to(message, f'Введенное число больше загаданного')
        elif ent_num < num:
            bot.reply_to(message, f'Введенное число меньше загаданного')
        else:
            bot.reply_to(message, f'Вы угадали число {num} за {count} ходов')
            num = random.randint(0,1000)
            count = 0
            bot.reply_to(message, f'Загадано новое число')

    with open('log.txt', 'a', encoding='utf-8') as data:
        data.writelines(message.text+'\n')


bot.polling(non_stop=True, interval=0)
