linha1 = input().split(" ")
a, b, c = linha1

triangulo = (float(a) * float(c))/2
circulo = (float(c)**2) * 3.14159
trapezio = (float(a) + float(b))  * float(c)/2
quadrado = float(b) ** 2
retangulo = float(a) * float(b)

print('TRIANGULO: {:.3f}' .format(triangulo))
print('CIRCULO: %0.3f' %circulo)
print('TRAPEZIO: %0.3f' %trapezio)
print('QUADRADO: %0.3f' %quadrado)
print('RETANGULO: %0.3f' %retangulo)
