""""
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих
чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
4 4 -> 2 2
5 6 -> 2 3
"""

while True:
    try:
        S = int(input('введите сумму загаданных чисел: '))
        P = int(input('введите произведение загаданных чисел: '))
        flag = True
        for x in range(P):
            for y in range(P):
                if x+y == S and x*y == P:
                    print(f'x = {x}, y = {y}')
                    flag = False
                    break
        if flag:
            print('таких чисел не существует, введите заново')
        else:
            break       
    except:
        print('ошибка ввода типа данных, введите заново')