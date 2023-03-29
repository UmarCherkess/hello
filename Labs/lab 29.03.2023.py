#Задание 1
import itertools

lst = ['A','B']
combs = itertools.permutations(lst)

for comb in combs:
    print(comb)
 
#Задание 2
from itertools import product

lst1=['A','B','C']
lst2=['X','Y','Z']

cart_product = list(product(lst1,lst2))

print(cart_product)

#Задание 3
import itertools

lst1 = ['A','B']
lst2 = ['X','Y']
lst3 = ['1','2']

lst4 = list(itertools_product(lst1,lst2,lst3))

print(lst4)

#Задание 4 
import itertools

lst = ['A','B','C']

perm = list(itertools.product(lst,repeat=len(lst)))

print(perm)
           
#Задание 5
import itertools

sub=['A','B','C']
all_subs=[]

for sub_l in range(len(sub)+1):
  for a_sub in itertools.combinations(sub,sub_l):
      all_subs.append(set(a_sub))
  
  
print(all_subs)

#Задание 6
import itertools

str= 'ABC'

comb_lst=list(itertools.permutations(str))

for perm in comb_lst:
    print(''.join(perm))

#Задание 7
import itertools

str= 'ABC'

for i in range(len(str)):
    for p in itertools.product(str, repeat=i+1):
        print(''.join(p))

#Задание 8
import itertools

def pythagorean_troyki(max_val):
  for a, b, c in itertools.product(range(1, max_val), repeat=3):
    if a**2+b**2 == c**2:
      yield(a,b,c)

max_val = 20 
for troyki in pythagorean_troyki(max_val):
  print(troyki)

#Задание 9
import itertools


