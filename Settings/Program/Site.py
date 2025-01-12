
from Config.Util import *
from Config.Config import *
try:
    import webbrowser
except Exception as e:
   ErrorModule(e)

Title("Site")

print(f"""
 {BEFORE}01{AFTER}{white} Discord
 {BEFORE}02{AFTER}{white} Github
""")

try:
    choice = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Site -> {reset}")
    if choice in ['1', '01']:
        site = f"{discord_server}"
        webbrowser.open_new_tab(site)
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Access to the site \"{white}{site}{red}\"" + reset)
        Continue()
        Reset()

    if choice in ['2', '02']:
        site = f"https://{github_tool}"
        webbrowser.open_new_tab(site)
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Access to the site \"{white}{site}{red}\"" + reset)
        Continue()
        Reset()
except Exception as e:
    Error(e)
