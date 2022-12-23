while True:
    a = input('1 раздел:  +  ,  -  ,  *  ,  /  ,  :   ')
    if a == '+':
            b = float(input('Введите первое число: '))
            c = float(input('Введите второе число: '))
            print('Ответ:' + str (b+c))
    elif a == '-':
            b = float(input('Введите первое число: '))
            c = float(input('Введите второе число: '))
            print('Ответ:' + str (b-c))
    if a == '*':
            b = float(input('Введите первое число: '))
            c = float(input('Введите второе число: '))
            print('Ответ:' + str (b*c))
    elif a == '/':
            b = float(input('Введите первое число: '))
            c = float(input('Введите второе число: '))
            print('Ответ:' + str (b/c))
    while True:
        if a == '2 раздел':
            n = input('2 раздел: *? **    ***   √?   : ')
            if n == '**':
                b = float(input('Введите число: '))
                print('Ответ: ' + str(b*b))
            elif n == '***':
                b = float(input('Введите число: '))
                print('Ответ' + str (b*b*b))
            if n =='√':
                b = float(input('Введите число: '))
                f = 1
                while f*f != b:
                    f += 1
                else:
                    print('Ответ: ' + str (f))
            if n == '*?':
                o = int(input('В какой степени? '))
                e = int(input('Какое число? '))
                x = e**o
                print(x)

