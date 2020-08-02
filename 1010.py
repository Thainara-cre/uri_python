linha1 = input().split(" ")
linha2 = input().split(" ")

peca1, quant1, valor1 = linha1
peca2, quant2, valor2 = linha2

valortotal = (int(quant1) * float(valor1)) + (int(quant2) * float(valor2))

print('VALOR A PAGAR: R$ %0.2f'%valortotal)

