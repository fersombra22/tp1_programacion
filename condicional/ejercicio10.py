#10)	Hacer un algoritmo que a partir de dos números ingresados se imprima un
# resultado según las siguientescondiciones.
#Sielprimeroesmayorqueel segundo,semostraráladivisiónentreprimero/segundo.
#Sielsegundoesmayorqueel primero,sesolicitaráingresaruntercernúmero, mostrandoporconsolalasumadelos3.
#Recordemosquenosepuededividirpor0.
#Teinvitoarealizarlavalidacióncorrespondienteparaevitarquenuestroprogramalanceunerrorsiel 
#segundonúmeroesiguala0
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número (distinto de 0): "))
while num2 == 0:
    print("El segundo número no puede ser 0.")
    num2 = int(input("Ingrese un número distinto de 0: "))
if num1 > num2:
    div = num1 / num2
    print(f"El resultado de la división entre {num1} y {num2} es {div}")
else:
    num3 = int(input("Ingrese un tercer número: "))
    suma = num1 + num2 + num3
    print(f"La suma de {num1} + {num2} + {num3} es {suma}")
