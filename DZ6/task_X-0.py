#крестики нолики

def PrintMatrix(matrix): 
    print('')
    text = ' '+" │ ".join([str(i) for i in matrix[0:3]])+' '
    print(text.replace(' 0 ', '\033[1;31m 0 \033[0m').replace(' X ', '\033[1;32m X \033[0m'))
    print('───┼───┼───')
    text = ' '+" │ ".join([str(i) for i in matrix[3:6]])+' '
    print(text.replace(' 0 ', '\033[1;31m 0 \033[0m').replace(' X ', '\033[1;32m X \033[0m'))
    print('───┼───┼───')
    text = ' '+" │ ".join([str(i) for i in matrix[6:9]])+' '
    print(text.replace(' 0 ', '\033[1;31m 0 \033[0m').replace(' X ', '\033[1;32m X \033[0m'))
    print('')

def Check(matrix):
    if  (matrix[0]==matrix[1]==matrix[2] or
         matrix[3]==matrix[4]==matrix[5] or
         matrix[6]==matrix[7]==matrix[8] or
         matrix[0]==matrix[3]==matrix[6] or
         matrix[1]==matrix[4]==matrix[7] or
         matrix[2]==matrix[5]==matrix[8] or
         matrix[0]==matrix[4]==matrix[8] or
         matrix[2]==matrix[4]==matrix[6]): return True
    return False

import random
Matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]
PrintMatrix(Matrix)

end = False
while (end == False):
    try:
        InputNum = int(input('Ваш ход: '))
        if (InputNum>0) & (InputNum<10) & (Matrix[InputNum-1] not in ['0', 'X']):
            Matrix[InputNum-1] = 'X'
            PrintMatrix(Matrix)
            if Check(Matrix):
                print(' Вы выграли !!!')
                end = True
            elif len(set(Matrix))==2:
                print(' Ничья ')
                end = True
            else:
                InputNum = random.choice([i for i in Matrix if i not in ['0', 'X']])
                print('Ход ИИ: ', InputNum)
                Matrix[InputNum-1] = '0'
                PrintMatrix(Matrix)
                if Check(Matrix):
                    print(' ИИ выграл, вы продули')
                    end = True
            #break
        else:
            print('ошибка ввода числа (уже занято или от 1 до 9)') 
    except:
        print('ошибка ввода типа данных, введите заново')