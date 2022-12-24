import math
t = input("1 , 2 , 3")
if t == "1":
    while True:
        a = input('1 section:  +  ,  -  ,  *  ,  /  ,  :   ')
        if a == '+':
            b = float(input('Number 1: '))
            c = float(input('Number 2: '))
            print("Answer:" + str (b+c))
        elif a == '-':
            b = float(input('Number 1: '))
            c = float(input('Number 2: '))
            print('Answer:' + str (b-c))
        if a == '*':
            b = float(input('Number 1: '))
            c = float(input('Number 2: '))
            print("Answer:" + str (b*c))
        elif a == '/':
            b = float(input('Number 1: '))
            c = float(input('Number 2: '))
            print("Answer:" + str (b/c))
elif t == "2":
    while True:
        if a == '2 section':
            n = input('2 section: *? **    ***   √?   : ')
        if n == '**':
            b = float(input('Number: '))
            print('Answer: ' + str(b*b))
        elif n == '***':
            b = float(input('Number: '))
            print('Answer' + str (b*b*b))
        if n =='√':
            b = float(input('Number: '))
            f = 1
            while f*f != b:
                 f += 1
            else:
              print('Answer: ' + str (f))
        if n == '**?':
            o = int(input('**? '))
            e = int(input('Number: '))
            x = e**o
            print(x)
else:
    while True:
        l = input("3 section: module , factorial , pi , e :")
        if l == "module":
            b = float(input('Number: '))
            q = math.fabs(b)
            print(q)
        elif l == "factorial":
            b = int(input('Number: '))
            q = math.factorial(b)
            print(q)
        if l == "pi":
            q = math.pi
            print(q)
        elif l == "e":
            q = math.e
            print(q)
