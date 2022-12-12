import telebot

import config
import commands.send_pics
import misc_handlers.default_message_handler

bot = telebot.TeleBot(config.token)
print("Bot is online!")


@bot.message_handler(commands=['send_pics'])
def h_send_pics(message):
    commands.send_pics.send_pics_handler(bot, message)


@bot.message_handler(commands=['send_n_pics'])
def h_send_n_pics(message):
    commands.send_pics.send_n_pics_handler(bot, message)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    misc_handlers.default_message_handler.handle(bot, message)


bot.polling(none_stop=True, interval=0)
