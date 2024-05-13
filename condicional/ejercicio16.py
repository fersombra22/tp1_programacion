#16)	Escribirunprogramaqueleauncaráctereindiquesiesonounavocal.

caracter=input("ingrese un carater: ")
if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u":
    print(f"el caracter ingresado es una volca: {caracter}")
else:
    print(f"el caracter ingresado no es una vocal: {caracter}")