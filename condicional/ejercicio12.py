#12Una profesora de matemáticas le pide a su alumno con conocimientos de programación 
#que elabore unalgoritmoque,ingresandounnúmero,detectesiesteesnegativo,positivo,
#oiguala0.Utilicelascondicionesnecesariasparadesarrollarel
#algoritmocorrectamente.

num=int(input(" ingrese un numero "))
if num > 0:
    print(f"el numero ingresado es: {num} , es  positivo ")
elif num < 0:
        print(f"el numero ingresdo es {num} , es negativo")
else:
            print(f"el numero ingresado {num} ,  es igual a 0")

