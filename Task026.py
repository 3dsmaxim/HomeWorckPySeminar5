def EnterNumber(n):
    while True:
        try:
            if int(n) < 0:
                n = input('Введите целое положительное число: ')
            if int(n) >= 0:
                break

        except:
            n = input('Нам нужно число, повторите ввод: ')
    return int(n)


def math(num, num2):
        if num2 == 0:
            return 1
        if num2 != 0:
            return num*(math(num, num2-1))


numberFyrst = EnterNumber(input('Введите первое число: '))
numberSecond = EnterNumber(input('Введите второе число: '))

print(f'{numberFyrst} взведенное в степень {numberSecond} равно {math(numberFyrst, numberSecond)}')

