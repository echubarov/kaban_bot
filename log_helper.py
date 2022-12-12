import os
from datetime import datetime, timedelta
import config

log_rcv_path = f"{config.log_dir}/{config.log_rcv}"


def log_rcv(message):
    time = (datetime.utcfromtimestamp(int(message.date)) + timedelta(hours=3)).strftime('%Y-%m-%d %H:%M:%S')
    username = f"{message.from_user.first_name} {message.from_user.last_name}";
    log_entry = (f"{time}: | "
                 f"MESSAGE_ID = {message.id:<8} | "
                 f"USER = {message.from_user.id:<10} | "
                 f"NAME = {username:<30} | "
                 f"TEXT = \"{message.text}\"")
    print(log_entry)

    if not (os.path.exists(config.log_dir)):
        os.makedirs(config.log_dir)
    with open(log_rcv_path, "a") as f_log_rcv:
        f_log_rcv.write(f"{log_entry}\n")
