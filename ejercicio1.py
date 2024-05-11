#1.	EscribaunprogramaenPythonparaconvertirsegundosaminutos,minutosahorasyhorasadías.

print("ingrese la cantidad de segundos")
segundos=int (input())

horas = segundos / 3600
minutos = segundos / 60
dias = segundos / 86400

print (f" el resultado de segundos a horas es: {int(horas)} hora/s")
print(f" el resultado de segundos a minutos es: {int(minutos)} minuto/s")
print(f" el resultado de segundos a dias es: {(dias)}")
