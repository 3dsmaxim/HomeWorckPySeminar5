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


def sum(num, num2):
        if num2 == 0:
            return num
        else:
            return sum(num + 1, num2 - 1)


numberFyrst = EnterNumber(input('Введите первое число: '))
numberSecond = EnterNumber(input('Введите второе число: '))
print(f'{numberFyrst} + {numberSecond} = {sum(numberFyrst, numberSecond)}')
