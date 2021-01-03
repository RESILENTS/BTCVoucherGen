import requests
import random
chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number = input('[❌] Введите количество ссылок для генерации:'+ "\n")
length = input('[❌] Введите длинну ваучера (по стандарту '+ "\n")
btc_link = 'https://t.me/Chatex_bot?start=c_'
number = int(number)
length = int(length)
for n in range(number):
   password =''
   for i in range(length):
       password += random.choice(chars)
   print(btc_link + password)
