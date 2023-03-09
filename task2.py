""""
Найдите сумму цифр трехзначного числа. 
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""

flag = bool(True)
while flag:
    N = input('введите трехзначное число: ')
    if N.isdigit() == False:
        print('ошибка ввода типа данных, введите заново')
    elif int(N) >= 100 and int(N) < 1000:
        flag = False
    else:
        print('введено не трехзначное число, введите заново')

print(f'{N} -> {int(N[0])+int(N[1])+int(N[2])} ({int(N[0])} + {int(N[1])} + {int(N[2])})')