import random

print('➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖');
chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number = int(input('количество паролей?'+ "\n"))

btc_link = 'link'

length = int(input('длина пароля?'+ "\n"))
for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(chars)

print("btc_link", password)
