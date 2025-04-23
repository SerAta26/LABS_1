def calculator():

    """
Эта функция используется для выполнения операций над числами
введенных пользователем
    """

    print('Привет! Я калькулятор!')
    print()
    while True:
        try:
            num_1 = float(input('Введи первое число: '))
            num_2 = float(input('Введи второе число: '))
            operation = input('Какое действие выполняем? (+, -, *, /, //, %, **): ')

            if operation not in ['+', '-', '*', '/', '//', '%', '**']:
                raise ValueError('Выбери только действия из предложенных.')

            if operation == '+':
                result = num_1 + num_2
            elif operation == '-':
                result = num_1 - num_2
            elif operation == '*':
                result = num_1 * num_2
            elif operation == '/':
                if num_2 == 0:
                    raise ZeroDivisionError('Деление на ноль недопустимо.')
                result = num_1 / num_2
            elif operation == '//':
                if num_2 == 0:
                    raise ZeroDivisionError('Деление на ноль недопустимо.')
                result = num_1 // num_2
            elif operation == '%':
                result = num_1 % num_2
            elif operation == '**':
                result = num_1 ** num_2


            print('Результат:', result)
            break

        except ValueError as error:
            print('Ошибка ввода!:', error)
        except ZeroDivisionError as error:
            print('Ошибка:', error)


calculator()