'''
Realiza una función reverse que reciba una lista y devuelva una nueva lista cuyo contenido 
sea igual a la original pero invertida. Así, dada la lista [‘Di’, ‘buen’, ‘día’, ‘a’, ‘papa’], 
deberá devolver [‘papa’, ‘a’, ‘día’, ‘buen’, ‘Di’].

oracion.reverse()
'''

oracion = ["Di", "buen", "día", "a", "papá"]
invertida = []

def inversion_tosca(oracion):  #esta fue la opción más tosca y rápida que saqué, pero solo es valida para este caso concreto.
    inversion = oracion[4], oracion[3], oracion[2], oracion[1], oracion[0]
    
    return inversion




def inversion(oracion):   
    invertida = []
    for i in oracion:
        invertida = [i] + invertida
    
    return invertida



print(oracion)
print()
print (inversion_tosca(oracion))
print()
print (inversion(oracion))


