#Pedir 3 números por pantalla al usuario. Devolver un mensaje que incluya la suma de los 3 números ytambiénunmensajequedigasidichoresultadocontiene3omáscifras,caso contrario, mostrarelresultadoy"contienemenosde3cifras".
#Ejemplo: Resultado de la suma: 102, contiene 3 o más cifras.Ejemplo2:Resultadodelasuma:45,contienemenosde3cifras.
#Hacer lo mismo para la multiplicación de los 3 números, pero en vez de devolver si la cantidad de cifras esmayora3ono,devolversiel resultadoesmúltiplode2.
#Ejemplo: Resultado de la multiplicación: 1892, es múltiplo de 2.Ejemplo2:Resultadodelamultiplicación:103,noesmúltiplode2.

print("ingrese 3 numero")
num1=int(input())
num2=int(input())
num3=int(input())
suma=num1+num2+num3
print(f" el resultado de la suma de los 3 numero es: {suma}")
if suma>=100:
    print(f" el resultado contiene 3 o mas")
    multiplicacion=num1*num2*num3
    if multiplicacion % 2==0:
        print(f"el resultado de la multiplicacion es: {multiplicacion} , es multiplo de 2  ")
    else:
        print(f"el resultado no es: {multiplicacion} ,no es multiplo de 2 ")
else:
    print(f"el resultado es: {suma} , contiene menos de 3 cifras ")
