#11)	Una reconocida empresa de la ciudad necesita de sus servicios como programador, 
#necesitan un sistemaque calcule el sueldo de los empleados,
#el cual es20000 para aquellos empleados que llevan hasta 3meses(inclusive),
#yluegodelos3meses,eldoble. Elsistemarequiereingresarnombreyapellidodelempleadoytiempodeantigüedadenmeses,
#muestresusueldosegúncorresponda

nombre=input("ingrese el nombre del empleado: ")
apellido=input(" ingrese el apellido del empleado: ")
antiguedad=int (input("ingrese la antiguedad en meses del empleado"))
if antiguedad<=3:
    print(f"el sueldo de: {nombre}, {apellido} es de $ 20000")
else:
    print(f"el sueldo de {nombre}, {apellido}, es de: $40000")