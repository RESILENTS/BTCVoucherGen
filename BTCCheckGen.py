import random

print(' ')
print('➖➖➖➖➖➖➖[ BTCCheckGen 1.1 ]➖➖➖➖➖➖➖')
print(' ')
print('❌ Генератор BTC чеков')
print('❌ Скрипт написан для канала ТЕНЕВОЙ БИЗНЕС')
print('❌ Автор: t.me/resilents | Наши проекты: t.me/shadowbiznes')
print(' ')
print('➖➖➖➖➖➖➖[ BTCCheckGen 1.1 ]➖➖➖➖➖➖➖')
print()
print('[BTCCheckGen] Выберите для какого бота генерировать чеки:')
print()
print('1️⃣ BTC_EXCHANGE_BOT')
print('2️⃣ CHATEX_BOT')
print()
inp = input("[BTCCheckBot] Ваш выбор: ")

if inp == '1':
chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number = input('[BTCCheckGen] ➕ Укажите желаемое количество ссылок для генерации:'+ "\n")
print(' ')
number = int(number)
length = '32'
print(' ')
print('➖➖➖➖➖➖➖[ BTCCheckGen 1.1 ]➖➖➖➖➖➖➖')
print(' ')
print('[BTCCheckGen] ✅ Работа скрипта успешно завершена: ', number, ' чеков сгенерировано.')
print('➖➖➖➖➖➖➖[ BTCCheckGen 1.1 ]➖➖➖➖➖➖➖')
print(' ')
for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(chars)
    print('https://t.me/BTC_CHANGE_BOT?start=b_',password)


elif inp == '2':
chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number = input('[BTCCheckGen] ➕ Укажите желаемое количество ссылок для генерации:'+ "\n")
print(' ')
number = int(number)
length = '32'
print(' ')
print('➖➖➖➖➖➖➖[ BTCCheckGen 1.1 ]➖➖➖➖➖➖➖')
print(' ')
print('[BTCCheckGen] ✅ Работа скрипта успешно завершена: ', number, ' чеков сгенерировано.')
print('➖➖➖➖➖➖➖[ BTCCheckGen 1.1 ]➖➖➖➖➖➖➖')
print(' ')
for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(chars)
    print('https://t.me/BTC_CHANGE_BOT?start=b_',password)
else:
    print("[ProxyGo] ⛔ Произошла ошибка! Повторите попытку.")
toexit = input("[ProxyGo] ⚠️ Нажмите любую клавишу для завершения.")
