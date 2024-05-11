#3.	Escriba un programa en Python que calcule las raíces de una ecuación,
#usando la ecuación de segundogrado.

import math
a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))
raiz_discriminante = math.sqrt(b**2 - 4*a*c)
x1 = (-b + raiz_discriminante) / (2*a)
x2 = (-b - raiz_discriminante) / (2*a)
print("x1 es:", x1)
print("x2 es:", x2)