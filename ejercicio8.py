#8.	Escriba un programa en Python que pida al usuario dos números y muestra la “distancia”
#entre ellos (elvalorabsolutodesudiferencia,demodoqueel resultadoseasiemprepositivo).
#Usar función de valor absoluto

print("ingrese un numero")
num1=int(input())
print("ingrese un segundo numero")
num2=int(input())
distancia=abs(num1-num2)
print(f"la distancia que hay entre ellos es: {distancia}")