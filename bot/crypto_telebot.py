import telebot
import webbrowser
from config import Config

bot = telebot.TeleBot(Config.CRYPTO_TELEBOT_API_KEY)

@bot.message_handler(commands=['start', 'sex'])
def start(message):
    bot.send_message(message.chat.id, 'Hello!')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'FUCK YOU')

@bot.message_handler(commands=['site'])
def site(message):
    bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=romuMntrUPs&ab_channel=N%C3%BCbel-Topic')
    webbrowser.open('https://www.youtube.com/watch?v=romuMntrUPs&ab_channel=N%C3%BCbel-Topic')


@bot.message_handler()
def info(message):

    if message.text.lower() == 'sokal':
        bot.send_message(message.chat.id, f'Привіт {message.from_user.first_name}')
    elif message.text.lower() == 'andrii':
        bot.send_message(message.chat.id, f'Привіт {message.from_user.id}')



#bot.polling(none_stop=True)
bot.infinity_polling()