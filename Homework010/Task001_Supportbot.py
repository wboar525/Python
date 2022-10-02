import telebot
import random

bot = telebot.TeleBot("5589526179:AAGUKyWxY7d5gP67X3fBHLrnL0Q0RyrKWrE", parse_mode=None)

markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
btn1 = telebot.types.KeyboardButton('/registration')
btn2 = telebot.types.KeyboardButton('/notify')
btn3 = telebot.types.KeyboardButton('/ask')
markup.add(btn1, btn2, btn3)

hash = random.getrandbits(128)
print(hash)
print("hash value: %032x" % hash)

@bot.message_handler(commands=['start'])
def start(message):
	text = message.text
	print(f'{message.from_user.first_name} {message.from_user.last_name}: {text}')
	bot.send_message(message.from_user.id, "Choose one letter:", reply_markup=markup)

@bot.message_handler(commands=['ask']) # Задача №1
def ask_question(message):
	bot.send_message(message.from_user.id, "Задайте свой вопрос поддержке:")
	user = str(message.from_user.id)
	@bot.message_handler(content_types=["text", "sticker"])
	def get_text(message):
		question = str(message.text)
		with open('questions.txt', 'a', encoding='utf-8') as file:
			file.writelines(f'{user}\n{question}\n') 
		bot.reply_to(message, f'Вопрос сохранен в базе и передан в поддержку')

@bot.message_handler(commands=["registration"])
def reg(message):
	userdata = str(message.from_user.id) + '\n'
	with open('log.txt', 'r+', encoding='utf-8') as file:
		text_id = file.readlines()
		if userdata not in text_id:
			file.writelines(userdata)
			bot.reply_to(message, f'Регистрация прошла успешно')
		else:
			bot.reply_to(message, "Пользователь с таким id уже зарегистрирован")

@bot.message_handler(commands=["notify"])
def notify(message):
	with open('log.txt', 'r', encoding='utf-8') as file:
		users = list(file.readlines())
		for i in range(0,len(users)):
			users[i] = users[i].removesuffix('\n')
		users = list(set(users)) # уберем повторы
		for id in users:
			bot.send_message(int(id), "Скоро Новый год!")

bot.polling(none_stop=True, interval=0)