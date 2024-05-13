#1)	Realizarunprogramaquepidadosnúmerosporpantalla,
#siel primernúmeroesmayor(>)alsegundo,restarel segundo número al primero y 
#mostrar el resultado por pantalla. Caso contrario,
#restar el primer número alsegundoymostrarresultadoporpantalla.
print("ingrese un numero")
num1=int(input())
print("ingrese un segundo numero")
num2=int(input())
if num1 > num2:
     resultado=num1-num2
     print(f"el resultado de restar {num1} con {num2} es: {resultado}")
else:

     resultado=num2-num1
     print(f"el resultado de restar {num2} con {num1} es: {resultado}")

