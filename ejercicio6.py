#6.	EscribaunprogramaenPythonquecalculelalongituddeunacircunferenciaderadioconocido.
import math
print("ingrese la circunferencia ")
circunferencia = float(input())
long= (2*math.pi*circunferencia)
print(f" la longitud de la circunferencia es: {float(long)}")