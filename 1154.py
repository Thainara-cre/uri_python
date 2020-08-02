idade = int(input())
media = 0
soma = 0
cont = 0

while idade>0:
    soma += idade
    cont += 1
    idade = int(input())

media = soma/cont

print('{:.2f}'.format(media))
