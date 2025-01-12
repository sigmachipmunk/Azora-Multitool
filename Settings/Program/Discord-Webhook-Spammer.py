

from Config.Util import *
from Config.Config import *
try:
    import requests
    import json
    import threading
except Exception as e:
   ErrorModule(e)
   
Title("Discord Webhook Spammer")

try:
    webhook_url = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Webhook URL -> {reset}")
    CheckWebhook(webhook_url)
    message = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Message -> {reset}")

    try:
        threads_number = int(input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Threads Number -> {reset}"))
    except:
        ErrorNumber()

    def send_webhook():
        headers = {
            'Content-Type': 'application/json'
        }
        payload = {
            'content': message,
            'username': username_webhook,
            'avatar_url': avatar_webhook
        }
        try:
            response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))
            response.raise_for_status()
            print(f"{BEFORE_GREEN + current_time_hour() + AFTER_GREEN} {GEN_VALID} Message: {white}{message}{color.GREEN} Status: {white}Send{color.GREEN}")
        except:
            print(f"{BEFORE + current_time_hour() + AFTER} {GEN_INVALID} Message: {white}{message}{red} Status: {white}Rate Limit{red}")

    def request():
        threads = []
        try:
            for _ in range(int(threads_number)):
                t = threading.Thread(target=send_webhook)
                t.start()
                threads.append(t)
        except:
            ErrorNumber()

        for thread in threads:
            thread.join()

    while True:
        request()
except Exception as e:
    Error(e)
