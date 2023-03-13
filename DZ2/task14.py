""""
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
10 -> 1 2 4 8
"""

while True:
    try:
        N = int(input('введите число N: '))
        if N > 0:
            degree = list()
            i=0
            rez = 2**i
            while rez<=N:
                degree.append(rez)
                i+=1
                rez = 2**i
            print(degree)
            break
        else:
            print('ошибка ввода количества, введите натуральное положительное число')            
    except:
        print('ошибка ввода типа данных, введите заново')
