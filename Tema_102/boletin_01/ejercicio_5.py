'''
Realiza una función reverse que reciba una lista y devuelva una nueva lista cuyo contenido 
sea igual a la original pero invertida. Así, dada la lista [‘Di’, ‘buen’, ‘día’, ‘a’, ‘papa’], 
deberá devolver [‘papa’, ‘a’, ‘día’, ‘buen’, ‘Di’].

oracion.reverse()
'''

oracion = ["Di", "buen", "día", "a", "papá"]

def inversion (oracion):
    inversion = oracion[4], oracion[3], oracion[2], oracion[1], oracion[0]
    
    return inversion


print (f"Inversión: {inversion(oracion)}")