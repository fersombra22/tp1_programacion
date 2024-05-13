#4Desarrolle un algoritmo que permita leer tres valores y almacenarlos en las variables
#numero1, numero2,numero3respectivamente.
#El algoritmodebeimprimircuál esel mayor.

print("ingrese un numero")
num1=int(input())
print("ingrese un segundo nuemero")
num2=int(input())
print("ingrese un tercer numero")
num3=int(input())
if num1>num2:
        if num1>num3:
                print (f"el mayor es: {num1}")
        else:
                print(f"el mayor es: {num3}")
else:
        if num2>num3:
                print(f"es mayor {num2}")
        else:
                print(f"el mayor es {num3}")
        