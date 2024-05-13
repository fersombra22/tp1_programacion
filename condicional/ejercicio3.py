#Larotiseríadelpueblonecesitasabersiposeeelstockmínimoparavenderpizzaselpróximofindesemana.
#Sabiendo que el número mínimo de stock es 50 pizzas. Codifique un programa que,
#ingresando el número destockdisponible,notifiquesisepodrávenderpizzaselfindesemana,
#casocontrarioindiqueelstockfaltante.
print("ingrese el numero actual de stock de pizzas")
cantidadPizzas=int(input())
if cantidadPizzas >=50:
        print("si se podra vender hay stcok suficiente")
else:
        stock= 50-cantidadPizzas
        print (f"lo sentimos, falta/n , {stock}  pizza/s para completar el faltante de stock. ")