

from Config.Util import *
from Config.Config import *
try:
    import webbrowser
except Exception as e:
   ErrorModule(e)

Title("Discord Invite Bot To Id")

try:
    Slow(discord_banner)
    try:
        IdBot = int(input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} ID bot -> {reset}"))
    except:
        ErrorId()

    invite_url = f'https://discord.com/oauth2/authorize?client_id={IdBot}&scope=bot&permissions=8'
    response = requests.get(invite_url)
    print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Invite Url: {white + invite_url} (status: {response.status_code})")

    choice = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Open in browser ? (y/n) -> {reset}")
    if choice in ['y', 'Y', 'Yes', 'yes']:
        webbrowser.open_new_tab(invite_url)
        Continue()
        Reset()
    else:
        Continue()
        Reset()
except Exception as e:
    Error(e)
