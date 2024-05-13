#Elaborar un programa que simule el inicio de sesión a un sistema. Si el usuario es:
#”ADMIN” y la clave “1234”escribir el siguiente mensaje en pantalla “ACCESO PERMITIDO” 
#caso contrario mostrar el mensaje “ACCESODENEGADO”.
print("ingrese usuario")
usuario=input()
print("ingrese contraseña")
contraseña=int(input())
if usuario=="admin" and contraseña==1234:
        print("ACCESO PERMITIDO")
else:
    print("ACCESO DENEGADO")
