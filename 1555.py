from math import pow

x = int(input())
y = int(input())

r = pow ((3 * x), 2) + pow (y, 2)
b = 2 * pow ((x * 2), 2) + pow ((5 * y), 2)
c = -100 * x + pow (y, 3)

if r > b & r > c:
    print ('Beto ganhou')
elif b > r & b > c:
    print('Carlos ganhou')
elif c > r & c > b:
    print('Rafael ganhou')
