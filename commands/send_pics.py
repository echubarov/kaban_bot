import random
import os
from os.path import isfile, join

from config import pics_dir
from log_helper import log_rcv


def send_pics_handler(bot, message):
    if not (os.path.exists(pics_dir)):
        bot.send_message(message.from_user.id, f"{pics_dir} directory does not exist!")
        return
    log_rcv(message)
    files = [f for f in os.listdir(pics_dir) if isfile(join(pics_dir, f))]
    if not files:
        bot.send_message(message.from_user.id, f"There are no pics in {pics_dir}!")
        return

    img = open(f"{pics_dir}/{random.choice(files)}", 'rb')
    bot.send_photo(message.from_user.id, img)


def send_n_pics_handler(bot, message):
    log_rcv(message)
    bot.send_message(message.from_user.id, "How many pics do you want?")
    bot.register_next_step_handler(message, send_n_pics_step_2, bot)


def send_n_pics_step_2(message, bot):
    log_rcv(message)
    count = 0
    try:
        count = int(message.text)
    except ValueError:
        bot.send_message(message.from_user.id, "Not a valid number, bruh")
        return
    if count < 0:
        bot.send_message(message.from_user.id, "Nice pic count, retard")
    else:
        if count == 1:
            bot.send_message(message.from_user.id, "You could just use the \"/send_pics\" command, you know")

        if not (os.path.exists(pics_dir)):
            bot.send_message(message.from_user.id, f"{pics_dir} directory does not exist!")
            return
        files = [f for f in os.listdir(pics_dir) if isfile(join(pics_dir, f))]
        if not files:
            bot.send_message(message.from_user.id, f"There are no pics in {pics_dir}!")
            return

        random.shuffle(files)
        res_files = files[:count]
        for file in res_files:
            img = open(f"{pics_dir}/{file}", 'rb')
            bot.send_photo(message.from_user.id, img)
