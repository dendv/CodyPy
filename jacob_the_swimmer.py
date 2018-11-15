# http://pythontutor.ru/lessons/ifelse/problems/jacob_the_swimmer/

N = int(input())
M = int(input())
x = int(input())
y = int(input())
if N==x or N==y or M==x or M==y or x==0 or y==0:
    print('0')
elif x<=M/2 and y>x:
    print(x)
elif x>M/2 and y>x:
    print(M-x)
else:
    print(y)
