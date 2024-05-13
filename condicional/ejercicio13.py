#13)	Desarrolle un algoritmo que a partir de dos números ingresados
#se realicen los siguiente cálculos según lassiguientescondiciones.
#Siel primernúmeroesunnúmeropositivodeberámostrarseporpantallalasumadeloscuadradosdeambosnúmeros.
#Siel primernúmeroesunnúmeronegativodeberámostrarseporpantallaelprimeroelevadoporelsegundo.
#Todoslosnúmerosdebenserenteros.Operadorpotencia->^(alt+94)

num1=float(input("ingrese un numero: "))
num2=float(input("ingrese un segundo numero: "))
if num1 > 0:
    suma=num1 ** 2+ num2 ** 2
    print(F"la suma de los cuadros de ambos numero es: {suma} ")
else:
    resultado = -(num1)**num2
    print(f"el resultado de elevar el primer numero por el segundo es: {resultado}")
