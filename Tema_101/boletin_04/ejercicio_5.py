numeroA=int(input("Inserte primera cifra: "))
numeroB=int(input("Inserte segunda cifra: "))

distancia=numeroA-numeroB

if( distancia < 0):
    distancia = distancia*-1
print(f"La distancia entre ambos numers es: {distancia}")
    