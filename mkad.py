# http://pythontutor.ru/lessons/int_and_float/problems/mkad/

V = int(input())
t = int(input())

# Решение разработчика:
# print((V * t) % 109)

if abs(V*t)>108:
    print(abs((V*t)%109))
else:
    print(109-abs(V*t))
