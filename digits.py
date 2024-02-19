def max_sum():
    digits = {}
    digit = 1

    while True:
        digit = input('Введите число: ')
        if digit.isdigit():
            sum = 0
            for i in digit:
                sum += int(i)
            digits[sum] = digit
            if int(digit) == 0:
                break
        else:
            print('Введите корректные данные(целое число)')

    key = sorted(digits.keys())[-1]
    result = digits[key]

    print(f'Число - {result}, сумма цифр - {key}')
    print('Чтобы закрыть программу введите повторно 0,\nчтобы запустить повторно 1')
    while True:
        word = input('Введите команду: ')
        if word == '1':
            return max_sum()
        if word == '0':
            return
        else:
            print('Введите корректные данные')


if __name__ == '__main__':
    max_sum()


