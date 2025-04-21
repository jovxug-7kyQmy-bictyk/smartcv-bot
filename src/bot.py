import telebot

TOKEN = 8035709336:AAGZwiwJRBstCbGtzhD8NFuc12KlJklef1U

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привіт! Я працюю. Чим можу допомогти?")

bot.polling()
