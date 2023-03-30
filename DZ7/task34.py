""""
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько 
легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, 
то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. 
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
Ввод: 
пара-ра-рам рам-пам-папам па-ра-па-дам 
Вывод:
Парам пам-пам
"""
string = 'пара-ра-рам ром-пюм-папам па-ра-па-дам'
VoweLettters = 'аеёиоуэюя'

list1 = []
for i in string.split(' '):
    list1.append(len(list(filter(lambda x: x in VoweLettters,''.join(i).lower()))))

if list1.count(list1[0]) == len(list1):
    print('Парам пам-пам')
else:
    print('Пам парам')