import telebot

# You can set parse_mode by default. HTML or MARKDOWN
bot = telebot.TeleBot(
    "5589526179:AAGUKyWxY7d5gP67X3fBHLrnL0Q0RyrKWrE", parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(content_types=["text", "sticker"])
def function_name(message):
	bot.reply_to(message, "This is a message handler")
    with open('log.txt', 'a', encoding='utf-8') as data:
        data.writelines(message.text)

bot.polling(non_stop=True, interval=0)

