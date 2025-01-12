

from Config.Util import *
from Config.Config import *
try:
    import requests
    import threading
except Exception as e:
   ErrorModule(e)
   
Title("Discord Token Leaver")

try:
    def leaver(guilds, token):
        for guild in guilds:
            try:
                response = requests.delete(f'https://discord.com/api/v8/users/@me/guilds/'+guild['id'], headers={'Authorization': token})
                if response.status_code == 204 or response.status_code == 200:
                    print(f"{BEFORE_GREEN + current_time_hour() + AFTER_GREEN} {GEN_VALID} Status: {white}Leave{green} Server: {white}{guild['name']}")
                elif response.status_code == 400:
                    response = requests.delete(f'https://discord.com/api/v8/guilds/'+guild['id'], headers={'Authorization': token})
                    if response.status_code == 204 or response.status_code == 200:
                        print(f"{BEFORE_GREEN + current_time_hour() + AFTER_GREEN} {GEN_VALID} Status: {white}Leave{green} Server: {white}{guild['name']}")
                else:
                    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Status: {white}Error {response.status_code}{red} Server: {white}{guild['name']}")
            except Exception as e:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Status: {white}Error: {e}{red}")
    

    Slow(discord_banner)
    token = Choice1TokenDiscord()

    processes = []
    guilds_id = requests.get("https://discord.com/api/v8/users/@me/guilds", headers={'Authorization': token}).json()
    if not guilds_id:
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} No Server found.")
        Continue()
        Reset()
    for guild in [guilds_id[i:i+3] for i in range(0, len(guilds_id), 3)]:
        leaver(guild, token)
    Continue()
    Reset()
except Exception as e:
    Error(e)
