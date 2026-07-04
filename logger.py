from datetime import datetime
import os

LOG_FOLDER = "logs"
LOG_FILE = os.path.join(LOG_FOLDER, "KAI_bot.log")

def log(message):
    current_time = datetime.now()

    log_message = f"[{current_time}] {message}"

    print(log_message)

    
    if not os.path.exists(LOG_FOLDER):
        os.makedirs(LOG_FOLDER)

    with open(LOG_FILE, "a") as file:
        file.write(log_message + "\n")