
from Config.Util import *
from Config.Config import *
try:
    import requests
except Exception as e:
   ErrorModule(e)
   

Title("Discord Webhook Delete")

try:
    webhook_url = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} URL Webhook -> {color.RESET}")
    CheckWebhook(webhook_url)
    try:
        response = requests.delete(webhook_url)
        response.raise_for_status()
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Webhook Deleted.")
        Continue()
        Reset()
    except:
        ErrorWebhook()
except Exception as e:
    Error(e)
