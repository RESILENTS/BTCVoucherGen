import random

print(' ')
print('➖➖➖➖➖➖➖[ BTCCheckGen 1.0 ]➖➖➖➖➖➖➖')
print(' ')
print('Генератор чеков для @BTC_CHANGE_BOT')
print('Скрипт написан для канала ТЕНЕВОЙ БИЗНЕС')
print('Автор: t.me/resilents | Наши проекты: t.me/shadowbiznes')
print(' ')
print('➖➖➖➖➖➖➖[ BTCCheckGen 1.0 ]➖➖➖➖➖➖➖')
print(' ')
chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number = input('◾ Укажите желаемое количество ссылок для генерации:'+ "\n")
print(' ')
length = input('◾ Укажите длинну чека (советуем ввести 32):'+ "\n")
print(' ')
number = int(number)
length = int(length)
print(' ')
print('☑ Работа скрипта успешно завершена: ', number, ' чеков сгенерировано.')
print('⚠️ ВНИМАНИЕ: Скрипт генерирует рандомные чеки, проверять на валидность придется вручную.')
print(' ')
for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(chars)
    print('https://t.me/BTC_CHANGE_BOT?start=b_'+password)
print(' ')
print('➕ Все новости и обновления скрипта в нашем телеграм канале, подпишись и не пропускай новые плюшки.')
print()
toexit = input("[BTCCheckGen] ⚠️ Нажмите любую клавишу для завершения.")
