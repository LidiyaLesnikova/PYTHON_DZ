""""
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих
чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
4 4 -> 2 2
5 6 -> 2 3
"""
import math

while True:
    try:
        S = int(input('введите сумму загаданных чисел до 1000: '))
        P = int(input('введите произведение загаданных чисел до 1000: '))
        flag = True

        # через цикл
        for x in range(S):
            for y in range(S):
                if x+y == S and x*y == P:
                    print(f'1) x = {x}, y = {y}')
                    flag = False
                    break
            # через условие
            if x*(S-x) == P:
                print(f'2) x = {x}, y = {S-x}')
                flag = False
        
        # '''
        # Через дискриминант квадратного уравнения: - НЕ РАБОТАЕТ!!!! (ВЫВОДИТ НЕВЕРНЫЕ ЗНАЧЕНИЯ)
        # x + y = S
        # x * y = P
        # (S — y) * y = P
        # y^2 — y * S + P = 0
        # '''
        # discriminant = int(S) * int(S) - 4 * int(P)
        # x1 = int((int(S) + int(math.sqrt(discriminant))) / 2)
        # y1 = int(S) - x1
        # print(f"3) {S} {P} -> {str(x1)} {str(y1)}")

        if flag:
            print('таких чисел не существует, введите заново')
        else:
            break            
    except:
        print('ошибка ввода типа данных, введите заново')

