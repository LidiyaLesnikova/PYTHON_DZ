""""
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи (Например имя или фамилию
человека)
4. Использование функций. Ваша программа не должна быть линейной

Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, 
и Вы должны реализовать функционал для изменения и удаления данных
"""
import os

def CreateDirectory(fileName):
    print('Формирование структуры справочника:')
    with open(fileName, 'w+', encoding="utf-8") as data:
        data.writelines('ID:LastName:FirstName:SecondName:Phone\n')
    with open(fileName, 'r', encoding="utf-8") as data:
        lines = data.readlines()
        str = lines[0].replace('\n','').split(':')
        print('{}\t\t{}\t\t{}\t\t{}\t\t{}'.format(str[0], str[1], str[2], str[3], str[4]))

def inputPhone():
    while True:
        Phone = input('Номер телефона: ')
        if len(Phone)!=9 or Phone.isdigit()==False: 
            print('ошибка ввода данных, введите 9-ти значный номер')
        else: return Phone

def ViewDirectory(fileName):
    try:
        with open(fileName, 'r', encoding="utf-8") as data:
            lines = data.readlines()
            if len(lines)==0:
                CreateDirectory(fileName)
            elif len(lines)==1:
                print('Справочник пустой')
            else:
                for i in range(1,len(lines)): 
                    str = lines[i].replace('\n','').split(':')
                    print('ID: {}\t\tФамилия: {}\t\tИмя: {}\t\tОтчество: {}\t\tНомер телефона: {}'.format(str[0], str[1], str[2], str[3], str[4]))
    except:
        print('справочник не существует, сначала надо его создать')


def InsertTelefone(fileName):
    try:
        if os.path.exists(fileName)==False:
            CreateDirectory(fileName)
        print('Введите данные справоника: ')
        LastName = input('Фамилия: ')
        FirstName = input('Имя: ')
        SecondName = input('Отчество: ')
        Phone = inputPhone()
        with open(fileName, 'r+', encoding="utf-8") as data:
            lines = data.readlines()
            if len(lines)==0 or len(lines)==1:
                ID = 1
            else:
                ID = int(lines[-1].split(':')[0]) + 1
            data.writelines(str(ID)+':'+ LastName.upper()+':'+ FirstName.upper()+':'+ SecondName.upper()+':'+ Phone+'\n')
            print('телефон добавлен')          
    except:
        print('ошибка ввода типа данных, введите заново')
        
def ModifyTelefone(fileName, Anser, mode = 0):
    try:
        if Anser != 0:
            with open(fileName, 'r', encoding="utf-8") as data:
                lines = data.readlines()
                ptr = 0
                with open(fileName, 'w', encoding="utf-8") as data1:
                    for i in range(0,len(lines)):
                        if i==0:
                            ID = 0
                        else:
                            ID = int(lines[i].split(':')[0])
                        if ID != Anser:
                            data1.write(lines[i])
                        elif ID == Anser and mode==1:
                            prnt = "Номер удален"
                        else: # ID == Anser:
                            print('Введите номер реквизита, который надо поменять:\n',
                                '1 - Фамилия \n',
                                '2 - Имя \n',
                                '3 - Отчество \n',
                                '4 - Телефон')
                            while True:
                                try:
                                    ModifyDetails = int(input('Ввод номера реквизита: '))
                                    if ModifyDetails == 4:
                                        NewDetails = inputPhone()
                                    else:
                                        NewDetails = input('Новое значение реквизита: ')
                                    Detail = lines[i].split(':')[ModifyDetails]
                                    data1.write(lines[i].replace(Detail,NewDetails.upper()))
                                    prnt = "Запись изменена"
                                    break
                                except:
                                    print('Неверный реквизит, номер 1-4')
        else: prnt = 'Такой записи нет в справочнике'
        print(prnt)
    except:
        print("Такой записи не существует")

def SearchTelefone(fileName):
    searchTel = input('Введите строку поиска записи в справочнике: ')
    try:
        with open(fileName, 'r', encoding="utf-8") as data:
            lines = data.readlines()
            if len(lines)==0 or len(lines)==1:
                print('Справочник пустой')
            else:
                count = 0
                for i in range(1,len(lines)):
                    if searchTel.upper() in lines[i]:
                        str = lines[i].replace('\n','').split(':')
                        print('ID: {}\t\tФамилия: {}\t\tИмя: {}\t\tОтчество: {}\t\tНомер телефона: {}'.format(str[0], str[1], str[2], str[3], str[4]))
                        count+=1
                if count==0:
                    print('запись не найдена')                 
    except:
        print('справочник не существует, сначала надо его создать')


telephoneDirectory = 'TelephoneDirectory.txt'

print('Введите действие:\n',
      '1 - просмотреть телефонный справочник \n',
      '2 - добавить в телефонный справочник номер \n',
      '3 - найти запись в телефонном справочнике \n',
      '4 - изменить запись в телефонном справочнике \n',
      '5 - удалить номер из справочника \n',
      '6 - закончить работу со справочником')

while True:
    try:
        Anser = int(input('Ввод действия со справочником: '))
        if Anser == 1: # просмотр справочника
            ViewDirectory(telephoneDirectory)
        elif Anser == 2: # добавить запись
            InsertTelefone(telephoneDirectory)
        elif Anser == 3: # найти запись
            SearchTelefone(telephoneDirectory)
        elif Anser == 4: # изменить запись
            try:
                ModifyLine = int(input('Введите ID, который надо изменить: '))
                ModifyTelefone(telephoneDirectory, ModifyLine)
            except:
                print("Такой записи не существует")                
        elif Anser == 5: # удалить запись
            try:
                DeleteLine = int(input('Введите ID, который надо удалить: '))
                ModifyTelefone(telephoneDirectory, DeleteLine, 1)
            except:
                print("Такой записи не существует")
        elif Anser == 6: # выход
            print('До свидания')
            break
        else:
            print('ошибка ввода данныых, введите число от 1 до 5')
    except:
        print('ошибка ввода типа данных, введите заново')
 