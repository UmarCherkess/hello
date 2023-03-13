#Задание 1
def sum(x, y):
    return x+y

print (sum(1, 2))

#Задание 2
a = [1, 2 , 3, 4]
def maxx(a):
    return max(a)

print(maxx(a))

#Задание 3

a = 'hello'
def vowels(a):
  vowelss = ['a','e','i','o','u']
  total = 0
  for s in a:
    if s in vowelss:
      total += 1
  return total

print(vowels(a))

#Задание 4 

a = 'pila'
b = 'lipa'
def anagram(a, b):
    str1 = list(a)
    str1.sort()
    str2 = list(b)
    str2.sort()
    return (str1 == str2)

print (anagram(a, b))

#Задание 5

str1 = 'Эта строка не являетя подстрокой'
str2 = 'Я подстрока!'
def podst(str1, str2):
  Count - str1.count(str2)
  if Count == 0:
    return 'Не подстрока'
  else:
    return 'Подстрока!'
 
print(podst(str1, str2)

#Задание 6 
str1 = 'Эта строка не являетя подстрокой'
str2 = 'Я являюсь подстрокой !'
def podst(str1, str2):
  Count = str1.count(str2)
  if Count == 0:
    return 'Не подстрока'
  else:
    return 'Подстрока!'
 
print(podst(str1, str2))
      
#Задание 7 
a = 1
b = 2
c = 3
def bigger(a, b, c):
      if a > b+c or b > a+c or c > a+b:
        return True
      else:
        return False
      
print(bigger(a, b, c))

#Задание 8 
a = 2
b = 2
c = 1
def equal(a, b, c):
      if a == b or a == c or b == a or b == c or c == b or c == a:
         return True
      else:
         return False
 
print(equal(a, b, c))

#Задание 9 
a = 'Ковалев'
b = 'Гедыгушев'
c = 'Дараев'
def nigger(a, b, c):
    if len(a) > len(b) + len(c) or len(b) > len(b) + len(a) or len(c) > len(b) + len(a):
         return True
    else:
         return False
      
print(nigger(a, b, c))
 
#Задание 10
a = 'Ковалев'
b = 'Гедыгушев'
c = 'Дараев'
def nigger(a, b, c):
    if len(a) == len(b) or len(a) == len(c) or len(b) == len(c): 
         return True
    else:
         return False
      
print(nigger(a, b, c))



