#Задание 1

import re 
result = re.search(r'Alabama','Sweet home Alabama')
print(result.group(0))

#Задание 2

import re 
result = re.sub(r'Alabama','Omaha','Sweet home Alabama')
print(result)

#Задание 3

import re 
result = re.findall(r'Bulka','Bulka s makom and Bulka s koritsey')
print(result)

#Задание 4

import re
result = re.match(r'Mr','Mr boombastic')
print(result.group(0))

#Задание 5

import re
result = re.split(r'a','Sweet home Alabama', maxsplit = 2) 
print(result)
