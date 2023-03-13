""""
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.
5 -> 1 0 1 1 0
2
"""
import random

flag = bool(True)
while True:
    try:
        N = int(input('введите количество монеток на столе: '))
        if N>0:
            monets = list()
            for i in range(int(N)):
                monets.append(random.randint(0, 1))
            """
            monets = [int(i) for i in str(N)]
            """
            print(monets)
            orel = 0 #0
            reshka = 0 #1
            for i in range(N):
                if monets[i]==0:
                    orel+=1
                else:
                    reshka+=1
            if orel==0 or reshka==0:
                print(f'переворачивать не надо, все одинаковые')
            elif orel==reshka:
                print(f'орел и решка равны, надо перевернуть {reshka} любой из них')
            elif orel>reshka:
                print(f'надо перевернуть {reshka} решки')
            else:
                print(f'надо перевернуть {orel} орлов')
            break
        else:
            print('ошибка ввода количества, введите натуральное положительное число0')            
    except:
        print('ошибка ввода типа данных, введите заново')



