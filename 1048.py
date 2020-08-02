salantigo = float(input())
novosal = 0
porcentagem = 0
reajuste = 0

if salantigo<=400.00:
    reajuste = salantigo * 0.15
    porcentagem = 15
elif salantigo <= 800.00:
    reajuste = salantigo * 0.12
    porcentagem = 12
elif salantigo <= 1200.00:
    reajuste = salantigo * 0.10
    porcentagem = 10
elif salantigo <= 2000.00:
    reajuste = salantigo * 0.07
    porcentagem = 7
else:
    reajuste = salantigo * 0.04
    porcentagem = 4

novosal = salantigo + reajuste

print('Novo salario: {:.2f}'.format(novosal))
print('Reajuste ganho: {:.2f}'.format(reajuste))
print('Em percentual: {:.0f} %'.format(porcentagem))