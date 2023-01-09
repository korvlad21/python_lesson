while True:

    try:
        enter = float(input('Введите число: '))
        print(100/enter)
    except ValueError:

        print('Вы ввели не число!!!')  

    except ZeroDivisionError:
        print('Делить на ноль нельзя')

    else:
        print('Пользователь молодец, с первого раза!!')    
    finally:
        print('вывод финали')
print('Всё норм') 