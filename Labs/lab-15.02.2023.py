Задача 1 

import random

m, n = 2, 2
matrix_2 = [[random.randint(-100, 100)
             for _ in range(n)]
             for _ in range(m)]
print(matrix_2)
print(max(matrix_2, key=sum))


matrix_2 = [list(filter(lambda x: x % 2 == 0 and x > 0, matrix))
            for matrix in matrix_2]
print(matrix_2)


min_matrix = [min(matrix)
              for matrix in matrix_2
                 if matrix]
print(min_matrix)

max_matrix = [max(matrix)
              for matrix in matrix_2
                 if matrix]
print(max_matrix)

print(min(min_matrix)) \
    if min_matrix \
      else print('В матрице нет четных элементов больше нуля')
print(max(max_matrix)) \
    if max_matrix \
      else print('В матрице нет четных элементов больше нуля')

Задача 2 + 3 + 4 

import random

m, n = 2, 2
matrix_2 = [[random.randint(-100, 100)
             for _ in range(n)]
             for _ in range(m)]
print(matrix_2)
print(max(matrix_2, key=sum))
print(min(matrix_2, key=sum))


matrix_2 = [list(filter(lambda x: x % 2 == 0 and x > 0, matrix))
            for matrix in matrix_2]
print(matrix_2)


min_matrix = [min(matrix)
              for matrix in matrix_2
                 if matrix]
print(min_matrix)

max_matrix = [max(matrix)
              for matrix in matrix_2
                 if matrix]
print(max_matrix)

print(min(min_matrix)) \
    if min_matrix \
      else print('В матрице нет четных элементов больше нуля')
print(max(max_matrix)) \
    if max_matrix \
      else print('В матрице нет четных элементов больше нуля')
