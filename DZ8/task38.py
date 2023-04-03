""""
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи (Например имя или фамилию
человека)
4. Использование функций. Ваша программа не должна быть линейной
"""
import os

def ViewDirectory(fileName):
    try:
        with open(fileName, 'r', encoding="utf-8") as data:
            lines = data.readlines()
            if len(lines)==0 or len(lines)==1:
                print('Справочник пустой')
            else:
                for i in range(1,len(lines),1): 
                    str = lines[i].split(';')
                    print('ID: {}\t\tФамилия: {}\t\tИмя: {}\t\tОтчество: {}\t\tНомер телефона: {}'.format(str[0], str[1], str[2], str[3], str[4]))
    except:
        print('справочник не существует, сначала надо его создать')


def InsertTelefone(fileName):
    try:
        if os.path.exists(fileName)==False:
            with open(fileName, 'a', encoding="utf-8") as data:
                data.writelines('ID;LastName;FirstName;SecondName;Phone\n')
        print('Введите данные справоника: ')
        LastName = input('Фамилия: ')
        FirstName = input('Имя: ')
        SecondName = input('Отчество: ')
        while True:
            Phone = input('Номер телефона: ')
            if len(Phone)!=9: 
                print('ошибка ввода данных, введите 9-ти значный номер')
            else: break
        with open(fileName, 'r+', encoding="utf-8") as data:
            lines = data.readlines()
            if len(lines)==0 or len(lines)==1:
                ID = 1
            else:
                ID = int(lines[-1].split(';')[0]) + 1
            data.writelines(str(ID)+';'+ LastName+';'+ FirstName+';'+ SecondName+';'+ Phone+'\n')
            print('телефон добавлен')          
    except:
        print('ошибка ввода типа данных, введите заново')
        
def DeleteTelefone(fileName):
    try:
        DeleteLine = int(input('Введите ID, который надо удалить: '))
        with open(fileName, 'a') as data:
            # reading line by line
            lines = data.readlines()
            ptr = 1
            with open(fileName, 'w') as data1:
                for line in lines:
                    if ptr != DeleteLine:
                        data1.write(line)
                    ptr += 1
        print("Номер удален")
    except:
        print("Такого номера не существует")


telephoneDirectory = 'TelephoneDirectory.txt'
print(os.path.abspath('task38.py'))

print('Введите действие:\n',
      '1 - просмотреть справочник \n',
      '2 - добавить в телефонный справочник номер \n',
      '3 - найти в телефонном справочнике номер \n',
      '4 - удалить номер из справочника \n',
      '5 - закончить работу со справочником')

while True:
    try:
        Anser = int(input('Ввод действия: '))
        if Anser == 1:
            ViewDirectory(telephoneDirectory)
        elif Anser == 2:
            InsertTelefone(telephoneDirectory)
        elif Anser == 3:
            #SearchTelefone(telephoneDirectory)
            print(2)
        elif Anser == 4:
            DeleteTelefone(telephoneDirectory)
        elif Anser == 5:
            print('До свидания')
            break
        else:
            print('ошибка ввода данныых, введите число от 1 до 5')
    except:
        print('ошибка ввода типа данных, введите заново')
 