import requests
import random
import os
import time

#Functions

def Posts(UserId:str):
    """
    Function to make petitions. 
    Being the first URL to search if user is online 
    and the second URL to get the Username from the ID
    """
    URLS = ['https://presence.roblox.com/v1/presence/users', f'https://users.roblox.com/v1/users/{UserId}']
    Body = {"userIds":[UserId]}
    Post = requests.post(url=URLS[0], json=Body)
    Get = requests.get(url=URLS[1])
    PResponse = Post.json()
    GResponse = Get.json()
    IsOnline = PResponse["userPresences"][0]["userPresenceType"]
    Name = GResponse["name"]
    DisplayName = GResponse["displayName"]

    return f"@{Name}",DisplayName,IsOnline
    
def Webhook():
    def url_valida(url):
        return "discord.com/api/webhooks" in url

    if not os.path.exists("UserData"):
        while True:
            WebhookURL = str(input("WebhookURL: "))
            if url_valida(WebhookURL):
                break
            print(rojo + "URL must be from discord..." + reset)
        with open(file="UserData", mode="w+") as f:
            if not f.writable():
                print(rojo + "File not writeable!" + reset)
            f.write(WebhookURL)
    else:
        print("It seems that there's already a URL. Do u wish to change?" + reset)
        choice = int(input(verde + "[1] Yes " + rojo + "[2] No " + reset))
        if choice < 0 or choice > 2:
            input(rojo + "WRONG OPTION!" + reset)
        elif choice == 1:
            while True:
                WebhookURL = str(input("New URL: "))
                if url_valida(WebhookURL):
                    break
                print(rojo + "La URL debe ser un webhook de Discord." + reset)
            with open(file="UserData", mode="w+") as f:
                f.write(WebhookURL)
        elif choice == 2:
            return
        return WebhookURL

def GETURL():
  if os.path.exists("UserData"):
        with open("UserData", mode="r") as f:
            contenido = f.read()
        return contenido
    
    

def PostWebhook(WebhookURL, UserName, Status, DISCORDID):
    if Status == 0:
        output = {
            "embeds":[{
            "title": "UsersScope",
            "description": f"{UserName} is offline...",
             "footer":{
              "text": "Bot by @axelitogamertv2"
            }
          }]
        }

    elif Status == 1:
        output = {
            "content": f"<@{DISCORDID}>",
            "embeds":[{
            "title": "UsersScope",
            "description": f"{UserName} is ONLINE!...",
            "color": 65535,
            "footer":{
              "text": "Bot by @axelitogamertv2"
            }
          }]
        }

    elif Status == 2:
        output = {
            "content": f"<@{DISCORDID}>",
            "embeds":[{
            "title": "UsersScope",
            "description": f"{UserName} is PLAYING!...",
            "color": 65280,
            "footer":{
              "text": "Bot by @axelitogamertv2"
            }
          }]
        }
    
    elif Status == 3:
        output = {
            "content": f"<@{DISCORDID}>",
            "embeds":[{
            "title": "UsersScope",
            "description": f"{UserName} is IN STUDIO!...",
            "color": 16753920,
            "footer":{
              "text": "Bot by @axelitogamertv2"
            }
          }]
        }



    try:
        response = requests.post(url=WebhookURL, json=output, timeout=5)
        response.raise_for_status()
    except Exception as e:
        print(rojo + f"Error enviando webhook: {e}" + reset)

#Decorations
verde = "\033[32m"
rojo = "\033[31m"
magenta = "\033[35m"
reset = "\033[0m"
banners = r"""
 ____ ___                            _________                           
|    |   \______ ___________  ______/   _____/ ____  ____ ______   ____  
|    |   /  ___// __ \_  __ \/  ___/\_____  \_/ ___\/  _ \\____ \_/ __ \ 
|    |  /\___ \\  ___/|  | \/\___ \ /        \  \__(  <_> )  |_> >  ___/ 
|______//____  >\___  >__|  /____  >_______  /\___  >____/|   __/ \___  >
             \/     \/           \/        \/     \/      |__|        \/ 
""", r"""
   __  __                    _____                     
  / / / /_______  __________/ ___/_________  ____  ___ 
 / / / / ___/ _ \/ ___/ ___/\__ \/ ___/ __ \/ __ \/ _ \
/ /_/ (__  )  __/ /  (__  )___/ / /__/ /_/ / /_/ /  __/
\____/____/\___/_/  /____//____/\___/\____/ .___/\___/ 
                                         /_/           
""", r"""
               .-')      ('-.  _  .-')    .-')     .-')                              _ (`-.    ('-.   
              ( OO ).  _(  OO)( \( -O )  ( OO ).  ( OO ).                           ( (OO  ) _(  OO)  
 ,--. ,--.   (_)---\_)(,------.,------. (_)---\_)(_)---\_)   .-----.  .-'),-----.  _.`     \(,------. 
 |  | |  |   /    _ |  |  .---'|   /`. '/    _ | /    _ |   '  .--./ ( OO'  .-.  '(__...--'' |  .---' 
 |  | | .-') \  :` `.  |  |    |  /  | |\  :` `. \  :` `.   |  |('-. /   |  | |  | |  /  | | |  |     
 |  |_|( OO ) '..`''.)(|  '--. |  |_.' | '..`''.) '..`''.) /_) |OO  )\_) |  |\|  | |  |_.' |(|  '--.  
 |  | | `-' /.-._)   \ |  .--' |  .  '.'.-._)   \.-._)   \ ||  |`-'|   \ |  | |  | |  .___.' |  .--'  
('  '-'(_.-' \       / |  `---.|  |\  \ \       /\       /(_'  '--'\    `'  '-'  ' |  |      |  `---. 
  `-----'     `-----'  `------'`--' '--' `-----'  `-----'    `-----'      `-----'  `--'      `------' 
"""

#Welcome
Messages = ["[+] Welcome to UsersScope!", "[+] Hello and welcome to UsersScope!", "[!] Whos the target?"]
print(random.choice(banners))
print(magenta + random.choice(Messages) + reset)
print(rojo + "Remember to give a UserId!" + reset)
UserId = input("UserId: ")
DiscordId = int(input("Give your user id of discord to ping when online.."))
Webhook()

#Core
while True:
  Result = Posts(UserId=UserId)
  PostWebhook(WebhookURL=GETURL(), UserName=Result[1], Status=Result[2], DISCORDID=DiscordId)
  print(f"DisplayName: {Result[0]}, Username: {Result[1]}, IsOnline?: {Result[2]}")
  time.sleep(120)