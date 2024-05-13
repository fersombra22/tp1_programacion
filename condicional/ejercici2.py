#2)	Realizarunprogramaque:
#a.	Pida3númerosquerepresentarannotasdealumnos
#b.	Calculeel promediodelosnúmeros
#c.	Siel promedioesmayoroiguala7,muestreporpantallael mensaje'APROBADO',caso contrario,mostrarel mensaje'DESAPROBADO'.

print("ingrese la primero nota del alumno")
nota1=int(input())
print("ingrese la segunda nota del alumno")
nota2=int(input())
print("ingrese la tercer nota del alumno")
nota3=int(input())

promedio= (nota1+nota2+nota3)/3
if promedio>=7:
     print(f"APROBADO {promedio}")
else:
     print(f"DESAPROBADO {promedio}")
