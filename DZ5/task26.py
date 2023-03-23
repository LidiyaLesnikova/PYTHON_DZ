'''
Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 
'''
def degree(a, b):    
    if b == 0: return 1 
    return a*degree(a, b-1)

while True:
    try:
        A = int(input('Введите число А '))
        B = int(input('Введите число B '))
        if B>=0:
            print(f'{A} в степени {B} -> {degree(A, B)}')    
        else:
            print(f'{A} в степени {B} -> {1/degree(A, -B)}')   
        break         
    except:
        print('ошибка ввода типа данных, введите заново')