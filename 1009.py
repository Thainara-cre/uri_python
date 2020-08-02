nome = input()
salario = float(input())
vendas = float(input())
comisao = vendas * 0.15
salarioFinal = salario + comisao

print('TOTAL = R$ %.02f' %salarioFinal)