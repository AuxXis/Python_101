'''
Escribir una función denominada encajan que indique si dos fichas de dominó encajan o no. 
Las fichas son recibidas en dos cadenas de texto con el siguiente formato
[3,4] [2,5]
'''
ficha1_1 = int(input("Inserte ficha 1_1: "))
ficha1_2 = int(input("Inserte ficha 1_2: "))
ficha2_1 = int(input("Inserte ficha 2_1: "))
ficha2_2 = int(input("Inserte ficha 2_2: "))

ficha1 = [ficha1_1, ficha1_2]
ficha2 = [ficha2_1, ficha2_2]

def encajan(ficha1, ficha2):   
    return ficha1 [0] in ficha2 or ficha1 [1] in ficha2
    



print (encajan(ficha1, ficha2))