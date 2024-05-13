#14)	Escribir un programa que lea dos números enteros desde el teclado y
#si el primero es mayor que el segundointercambie sus valores. 
#Nota: Si alguno de los dos valores ingresados por el usuario fue negativo,
#primerotransformarenpositivoantesdeintercambiarlo.
num1=int(input("ingrese un numero: "))
num2=int(input("ingrese el segundo numero: "))

if num1 < 0:
    num1 = abs(num1)
if num2 < 0:
    num2 = abs(num2)
if num1 > num2:
    num1, num2 = num2, num1
print("Después de los posibles intercambios:")
print("Primer número:", num1)
print("Segundo número:", num2)
