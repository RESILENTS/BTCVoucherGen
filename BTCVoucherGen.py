import secrets

number = int(input('количество паролей?' + "\n"))
length = int(input('длина пароля?' + "\n"))


def symbol():
    symbols = ([chr(s) for s in range(33, 127)])  # магия здесь
    return symbols


symbol()

for n in range(number):
    password = ''
    for i in range(length):
        password += secrets.choice(symbol())
    print(password)
