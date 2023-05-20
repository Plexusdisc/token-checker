import requests
from colorama import Fore, init
import json

init(autoreset=True)

print(Fore.BLUE+f"""
████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
   ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
   ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
   ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
» Made by plexus                                                                                                 
""")

token = input("Enter the token you want to check: ")
    
url = "https://discord.com/api/v9/users/@me"

headers = {"Authorization": token,
           "Content-Type": "application/json",
           "accept": "*/*",
           "accept-language": "en-US",
           "connection": "keep-alive",
           "sec-fetch-dest": "empty",
           "sec-fetch-mode": "cors",
           "sec-fetch-site": "same-origin",
           "referer": "https://discord.com/channels/@me",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36"}
client = requests.get(url=url, allow_redirects=False, headers=headers)


client_dict = client.json()

print(Fore.RED+"\n------------ Public account info ------------")
print(Fore.BLUE+f"Name & Discriminator: {client_dict['username']}#{client_dict['discriminator']}")
print(Fore.BLUE+f"ID: {client_dict['id']}")
if client_dict['bio'] == " " or client_dict['bio'] == "":
    print(Fore.RED+"Bio: This user has no bio")             # Yeah ik its a bit messed up, too many prints
else:
    print(Fore.BLUE + f"Bio: {client_dict['bio']}")
print(Fore.BLUE+f"Account profile picture: https://cdn.discordapp.com/avatars/{client_dict['id']}/{client_dict['avatar']}.png?size=1024")
print(Fore.BLUE+f"Account banner picture: https://cdn.discordapp.com/banners/{client_dict['id']}/{client_dict['banner']}.png?size=2048")
print(Fore.RED+"------------ Private account info ------------")
print(Fore.BLUE+f"Email: {client_dict['email']}")
print(Fore.BLUE+f"Account language: {client_dict['locale']}")

if client_dict["premium_type"] == 0:
    print("This user has no Nitro")
elif client_dict["premium_type"] == 1:
    print(Fore.BLUE+"This user has Nitro Basic/Boost")
elif client_dict["premium_type"] == 2:
    print(Fore.MAGENTA+"This user has Nitro Boost")
else:
    print(Fore.RED+"Unable to locate if this user has nitro!")