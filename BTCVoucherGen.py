import random
import requestsfrom colorama import Fore, Back, Style 

banner = Fore.YELLOW + Style.BRIGHT + """ \ __\ /\__ _\ /\ \ __/\ \ \ \/\ \ \/_/\ \/ \ \ \/\ \ \ \ \/_/\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \\ \ \ \ \ \_\ \__ \ \ \_/ \_\ \ \_\ \ 
by @li0ard [ovnl.in] | t.me/termuxmam / PIRATIKA

""" + Style.RESET_ALL 
print(banner)


chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number = int(input('количество паролей?'+ "\n"))

btc_link = 'link'

length = int(input('длина пароля?'+ "\n"))
for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(chars)
    print('ghh', password)
