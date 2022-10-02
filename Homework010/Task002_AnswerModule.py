#Задача 2. Добавьте боту модуль, который позволяет считывать из файла вопрос, 
#отвечать на него и отправлять ответ обратно пользователю.
import telebot

bot = telebot.TeleBot("5589526179:AAGUKyWxY7d5gP67X3fBHLrnL0Q0RyrKWrE", parse_mode=None)

with open('questions.txt', 'r', encoding='utf-8') as file:
	questions = list(file.readlines())

for i in range(0,len(questions)):
	questions[i] = questions[i].removesuffix('\n')

for i in range(0,len(questions)):
	id = questions[i]
	question = questions[i+1]
	print(f"Введите ответ на вопрос пользователя {id}: {question}")
	answer = input()
	bot.send_message(int(id), answer)




