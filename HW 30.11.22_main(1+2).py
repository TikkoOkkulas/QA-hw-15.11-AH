
N = int(input('Вкажіть натуральне число N = '))

if N !=0:
    print('Вывести треугольник #1 с шириной N с помощью цикла for')
else:
    print('invalid N')
"""
*****
****
***
**
*
"""
for i in range(N, 0, -1):
    print('*' * i)

if N !=0:
    print('Вывести треугольник #2 с шириной N с помощью цикла for')
"""
*
**
***
****
*****
"""
for i in range(N+1):
    print('*' * i)
