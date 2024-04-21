# # TODO опишите здесь функции для решения задачи

print('Добрый день!\nНиже написан код мини-калькулятора.\nПрошу ознакомиться и оценить\nЗаранее благодарю!')
def calc():
    while True:
        s = input('Введите один из указанных знаков +, -, *, /: ')
        if s in ('+', '-', '*', '/'):
            while True:
                try:
                    a = float(input('Введите первое число = '))
                    b = float(input('Введите второе число = '))
                except ValueError:
                    print('Вы ввели не число!')
                    continue
                break
            if s == '+':
                print(f'{a} + {b} = {a + b}')
            elif s == '-':
                print(f'{a} - {b} = {a - b}')
            elif s == '*':
                print(f'{a} * {b} = {a * b}')
            elif s == '/':
                try:
                    print(f'{a} / {b} = {a / b}')
                except ZeroDivisionError:
                    print('Делить на ноль нельзя!')
                    continue
        else:
            print('Неверный знак операции!')
            continue
        break

#  TODO запустите здесь все необходимые функции
if __name__ == '__main__':
    # Нужно для проверки
    calc()