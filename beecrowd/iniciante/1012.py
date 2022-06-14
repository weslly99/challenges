PI = 3.14159
a,b, c = [float(v) for v in input().strip().split()]
print("TRIANGULO: {:.3f}".format((a*c)/2)) 
print("CIRCULO: {:.3f}".format(PI * (c**2)))
print("TRAPEZIO: {:.3f}".format(((a+b)*c) / 2))
print("QUADRADO: {:.3f}".format(b**2))
print("RETANGULO: {:.3f}".format(a * b))