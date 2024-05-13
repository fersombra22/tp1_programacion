#Desarrolle un algoritmo que permita identificar que tan bueno fueron
#los números resultantes de dos dadosalserlanzados.Considerando:
#Silasumadeambosesiguala12mostrarporpantalla"ExcelenteTiro"
#Si la suma de ambos es igual o mayor a 7 y menor a 12 mostrar por pantalla
#"Buen Tiro"Silasumadeambosesmenora7mostrarporpantalla"MalaSuerte!"
#RETO EXTRA: Te animamos a validar también que ambos números ingresados sean correctos,
# es decir entre 1 y6(incluidos)
print("ingrese el numero que salio en el primer tiro")
tiro1=int(input())
while tiro1<1 or tiro1>6:
    print("error ingrese de nuevo el numero")
    tiro1=int (input())
print("el numero que salio en segundo lugar es")
tiro2=int(input())
while tiro2<1 or tiro2>6:
    print("error ingrese de nuevo el numero ")
    tiro2=int(input())
suma=tiro1+tiro2
if suma==12:
    print("excelente tiro")
else:
    if suma>=7 and suma < 12:
       print("buen tiro")
    
    else:
        if suma<7:
            print("mala suerte")





