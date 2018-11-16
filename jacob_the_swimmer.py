# http://pythontutor.ru/lessons/ifelse/problems/jacob_the_swimmer/

N = int(input())
M = int(input())
x = int(input())
y = int(input())

if N>=M:
    D = N
    K = M
else:
    D = M
    K = N
if x>K/2 and y>D/2: # I четверть
    if D-y>K-x:
        print(K-x)
    else:
        print(D-y)
if x>K/2 and y<D/2: # II четверть
    if y>K-x:
        print(K-x)
    else:
        print(y)
if x<K/2 and y<D/2: # III четверть
    if y>x:
        print(x)
    else:
        print(y)
if x<K/2 and y>D/2: # IV четверть
    if D-y>x:
        print(x)
    else:
        print(D-y)
