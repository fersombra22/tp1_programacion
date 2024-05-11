#9.	Escriba un programa en Python que nos diga
#el dinero que tenemos después de pedirnos cuantos billetestenemos
#(de$500,$100, $50,$10pesos).

print("ingrese la cantidad de billetes de $500")
num= int(input())
print("ingrese la cantidad de billetes de $100")
num1=int(input())
print("ingrese la cantidad de billetes de $50")
num2=int(input())
print("ingrese la cantidad de billetes de $10")
num3=int(input())

suma1=num*500
suma2=num1*100
suma3=num2*50
suma4=num3*10
suma=suma1+suma2+suma3+suma4
print(f"tenes $ {suma} pesos")