#15)	Escribir un programa que lea desde teclado el importe neto de una factura 
#y determine el importe finalsegúnlossiguientescriterios.
#Importenetomenorde10.000->sindescuento
#Importenetomayoroigualde10.000 ->15%dedescuento


importe=float(input("ingrese el importe neto de la factura: "))

if importe < 10000:
    importefinal=importe
    print(f"el importe sin descuento es de: {importefinal}")
else:
    importefinal=importe-(importe*0.15)
    print(f"el importe final con el descuento es: {importefinal}")
