#7)	Pedir al usuario por pantalla dos números y analizar lo siguiente:
#Si ambos son números pares mostrar porpantalla"PARES",delocontrario,
#sialgunodelosdosnúmerosesimpar,mostrarporpantalla"Unodelosdosnúmerosesimpar".
#Tipdeayuda:usaroperadorModparasabersiunnúmeroesparoimpar…
print("ingrese dos numeros")
num1=int(input())
num2=int(input())
if num1 % 2==0:
    if num2 % 2==0:
        print("los numeros son pares")
    else:
        print("los numeros son impares")
        
