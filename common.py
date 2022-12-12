import config


def get_user_id(message):
    return message.from_user.id


def is_verified_user(bot, user_id):
    for usr in config.auth_users:
        if str(user_id) == usr.id:
            return True
    bot.send_message(user_id, "This bot is private and you are not an authorized user")
    return False


def get_auth_user_name(user_id):
    for user in config.auth_users:
        if str(user_id) == user.id:
            return user.name
    return []


def get_callback_type(call):
    return call.data.split("_", 1)[0]


def exception_message(exc):
    return f"An exception occurred:\n`{str(exc)}`"
