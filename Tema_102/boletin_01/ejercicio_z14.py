'''
Escribe una función que, dada una lista de caracteres, devuelva la cadena más larga.
Si dos o más cadenas miden lo mismo y son las más largas, la función devolverá la
que tenga el mayor número de caracteres repetidos .
'''

cadena_1 = "bmw, mercedes, Audi, Opel, Volkswagen, Porsche"
cadena_2 = "Cadillac, Chevrolet, Chrysler, Ford, Hammer, Jeep"


def longitud(cadena1, cadena2):
    cadena1      
    if len(cadena1)<len(cadena2):
        cadena1=cadena2
    
    elif len(cadena1) == len(cadena2):
        list1 = []
        list2 = []
        for i in range(len(cadena1)):
            if cadena1[i] not in list1:
                list1.append(cadena1[i])
            if cadena2[i] not in list2:
                list2.append(cadena2[i])
        if len(list1) > len(list2):
            cadena1 = cadena2                                    
                
    return cadena1

print(f"es mas larga la cadena: {longitud(cadena_1, cadena_2)}")