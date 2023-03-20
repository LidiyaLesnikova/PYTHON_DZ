""""
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
Заполните массив случайными натуральными числами от 1 до N.
Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.
Ввод: 10
Ввод: 7
1 2 1 8 9 6 5 4 3 4
Вывод: 6
"""
import random

while True:
    try:
        N = int(input('введите количество элементов массива N: '))
        X = int(input('введите заданное число X: '))
        if N>0 and X>0:
            array = [random.randint(1, N) for _ in range(N)]
            print(array)
            arraySet= tuple(set(array))
            arrayDifference = [X-i for i in arraySet]
            if 0 in arrayDifference:
                print(f'Искомое число X = {X} есть в массиве, оно же ближайшее')
            else:
                arrPlus = [i for i in arrayDifference if i>0]
                arrMinus = [j for j in arrayDifference if j<0]
                if len(arrPlus)==0:
                    print(f'Искомое число X = {X}, ближайшее к нему {arraySet[arrayDifference.index(max(arrMinus))]}')
                elif len(arrMinus)==0:
                    print(f'Искомое число X = {X}, ближайшее к нему {arraySet[arrayDifference.index(min(arrPlus))]}')               
                else:
                    if min(arrPlus) <= abs(max(arrMinus)):
                        print(f'Искомое число X = {X}, ближайшее к нему {arraySet[arrayDifference.index(min(arrPlus))]}')
                    else:
                        print(f'Искомое число X = {X}, ближайшее к нему {arraySet[arrayDifference.index(max(arrMinus))]}')
            break
        else:
            print('ошибка ввода количества, введите натуральные положительные числа')            
    except:
        print('ошибка ввода типа данных, введите заново')