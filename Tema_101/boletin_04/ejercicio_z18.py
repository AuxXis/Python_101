'''
. Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite
inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine
el programa dará las siguientes informaciones:
◦ La suma de los números que están dentro del intervalo (intervalo abierto).
◦ Cuantos números están fuera del intervalo.
◦ Informa si hemos introducido algún número igual a los límites del intervalo.
'''

inferior = int(input("Introduce el límite inferior del intervalo: "))
superior = int(input("Introduce el límite superior del intervalo: "))

while inferior > superior:
    inferior = int(input("El límite inferior no puede ser mayor que el límite superior, introdúzcalo de nuevo: "))
   
numero = int(input(f"Introduzca un número entre {inferior} y {superior}: "))
    
suma = 0
fuera = 0
igual = 0

while numero != 0:
    numero = int(input(f"Introduzca un número entre {inferior} y {superior}: "))
    
    if inferior < numero < superior:
        suma += numero
    elif numero < inferior or numero > superior:
        fuera+=1
    else:
        igual=True
    
    numero = int(input(f"Introduzca un número entre {inferior} y {superior}: "))
                 
print (f"la suma de los números dentro del intervalo es {suma}, fuera del intervalo hay {fuera} números.")
if igual:
    print (f"Existe {igual} números que coinciden con los límites del intervalo.")


