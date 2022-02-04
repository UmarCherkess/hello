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
