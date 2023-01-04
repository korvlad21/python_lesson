import os

while True:
    sayt = input('Введите адрес сайта\n')

    if sayt == 'завершить':
        break

    if 'https://' in sayt:
        os.system('open ' + sayt)
        print('if')
    elif 'www.' in sayt:
        sayt = 'https://' + sayt
        os.system('open ' + sayt)
        print('elif')
    else:
        sayt = 'https://www.' + sayt
        os.system('open ' + sayt)
        print('else')        