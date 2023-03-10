""""
Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать 
один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
3 2 4 -> yes
3 2 1 -> no
"""
import random

def AvtoСhoice(n, m):
    return random.randint(n, m)

n = AvtoСhoice(2, 10)
m = AvtoСhoice(2, 10)
k = AvtoСhoice(2, 100)
if k>=n*m:
    print(f'У Шоколадки {n} x {m} -> нельзя отломить {k} долек, они больше всей шоколадки')
else:
    rez = 'нельзя'
    for i in range(n):
        if k==m*i:
            rez = 'можно'
            break
    for i in range(m):
        if k==n*i:
            rez = 'можно'
            break
    print(f'У Шоколадки {n} x {m} -> {rez} отломить {k} долек')
