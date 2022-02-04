Задание 1

stroka = input()
print(stroka[2])
print(stroka[-2])
print(stroka[:5])
print(stroka[:-2])
print(stroka[::2])
print(stroka[1::2])
print(stroka[::-1])
print(stroka[::-2])
print(len(stroka))

Задание 2 

print(input().count(' ') + 1) # т.к. счет идет с 0 в конце плюсуем 1

Задание 3 

stroka = input()
print(stroka[(len(stroka) + 1) // 2:] + stroka[:(len(stroka) + 1) // 2])

Задание 4 

stroka = input()
w1 = stroka[:stroka.find(' ')]
w2 = stroka[stroka.find(' ') + 1:]
print(w2 + ' ' + w1)

Задание 5 

s = input()
a = s.find('f')
b = s.rfind('f')
if a == -1:
    print()
elif a == b:
    print(a)
else:
    print(a, b)
    
Задание 6 

-

Задание 7 

stroka = input()

print(stroka[:stroka.find('h')] + stroka[stroka.rfind('h') + 1:])

Задание 8 

print(input().replace('1', 'one')) 

Задание 9 

print(input().replace('@', ''))

Задание 10  

stroka = input()
k = ''
for i in range(len(stroka)):
    if i % 3 != 0:
        k = k + stroka[i]
print(k)

Задание 11 

from math import sqrt
 
def rast(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
 
x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())
print(rast(x1, x2, y1, y2))

Задание 12 

def minimum(a, b, c, d):
    mas = [a,b,c,d]
    mas.sort()
    return mas[0]
 
print(min4(15,4,16,1))

Задание 13 

start = 1
end = -1
 
 
def IsPointInSquare(x, y):
    return (start >= x >= end) and (end <= y <= start)
 
 
x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print('DA')
else:
    print('NET')
    



