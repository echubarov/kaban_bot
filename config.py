import os
from dataclasses import dataclass


@dataclass
class User:
    id: str
    name: str


cwd = os.getcwd()
pics_dir = "pics"
log_dir = ".logs"
log_rcv = "log_rcv.log"

# Bot token. Get one from your Telegram bot info.
token = "your bot token here"

# Edit this list with user data.
auth_users = [
    User("user_id_0", "user_name_0"),
    User("user_id_1", "user_name_1")
]
