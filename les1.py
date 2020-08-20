# Настройки
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

proxies = {
    'http': 'socks5://localhost:9050',
    'https': 'socks5://localhost:9050'
}

url = "https://api.telegram.org"

out = requests.get(url, proxies=proxies).text

updater = Updater(token='736407448:AAFT1Mr0v-X36P7Iy7yyW59iVelto_JAqv4') # Токен API к Telegram
dispatcher = updater.dispatcher
# Обработка команд
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет, давай пообщаемся?')
def textMessage(bot, update):
    response = 'Получил Ваше сообщение: ' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)
# Хендлеры
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
# Начинаем поиск обновлений
updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()