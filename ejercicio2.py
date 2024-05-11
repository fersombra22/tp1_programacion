#2.	EscribaunprogramaPythonqueacepteelnúmerodeidentificacióndeunempleado,
#elsalarioporhoradel empleado y el total de horas trabajadas en un mes.
#Imprima la identificación y el salario delempleadodeunmesenparticular.

print("ingrese el numero de identificacion del empleado")
id= int(input())
print(" ingrese el saladrio por hora del empleado")
salarioHora=float(input())
print("ingrese el total de horas trabajadas por el empleado")
horasTrabajadas=int(input())
salario= float (salarioHora+horasTrabajadas) 

print(f" El trabajados nº: {id}")
print(f" El empleado gano $ {salario} este mes")