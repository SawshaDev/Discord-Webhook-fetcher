import requests
from colorama import init, Style, Fore
import os


option = input("Please choose an option! \n 1: Webhook Deleter ; 2: Webhook spammer ; 3: Webhook Checker: ")


if option == "1":
    os.system("cls")
    webhook_picker = input("Please enter the webhook link you want to delete: ") 
    
    r = requests.delete(webhook_picker)

    print("Deleted webhook!")

if option == "2":
    if os.name == 'nt':
        os.system('cls')
    print(f"{Fore.BLUE}Input Webhook URL to Spam: ",end='')
    HOOK_URL = input()
    print(f"{Fore.BLUE}What name should the webhook have?: ", end='')
    hook_username = input()
    print(f"{Fore.BLUE}Input Message to Spam: ", end='')
    message = input()
    print(f"{Fore.BLUE}How many times would you like to spam that (int)?: ", end='')
    times = int(input())
    hook_data = {
        "content" : f"{message}",
        "username" : f"{hook_username}"
        }
    once = 0
    print(Fore.GREEN + "Spamming now...")
    while once < times+1:
        requests.post(HOOK_URL, json = hook_data)
        once=once+1 


if option == "3":
    if os.name == 'nt':
        os.system('cls')
    print(f"{Fore.BLUE}Input Webhook URL to check: ",end='')
    HOOK_URL = input()

    r = requests.get(HOOK_URL)

    if r.status_code == 200:
        print("Webhook exists!")
    else:
        print("Yikes, for some reason (maybe it got deleted), The webhook does not exist or does not work!")
        
    

    


