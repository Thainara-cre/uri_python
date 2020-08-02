num1 = int(input())
num2 = int(input())

if num1 < num2:
    impares = [n for n in range(num1, num2) if n%2!=0]
else:
    impares = [n for n in range(num2, num1) if n%2!=0]
print(sum(impares))