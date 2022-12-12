import commands.send_pics
from log_helper import log_rcv
from common import get_auth_user_name


def handle(bot, message):
    log_rcv(message)
    if message.text == "Hi":
        bot.send_message(message.from_user.id, "Hi yourself")
    elif message.text == "send pics":
        commands.send_pics.send_pics_handler(bot, message)
    elif message.text == "test":
        bot.send_message(message.from_user.id, "no testing")
    elif message.text == "Проверка на гейство":
        response = []
        if get_auth_user_name(message.from_user.id) == "Крупик":
            response = "Ты гей"
        else:
            response = "Ты не гей"
        bot.send_message(message.from_user.id, response)

    else:
        bot.send_message(message.from_user.id, "To get Kaban pics type `send pics`", parse_mode="Markdown")
