'''
Diseña una función llamada estaOrdenada que reciba una lista de elementos y devuelva True si está ordenada
 o False en caso contrario
 
 '''

lista1 = [12,43,234,342,2133]
lista2 = [23,31,21,2,213,1,23]

def estaOrdenada(lista):
    ordenada = True
    for i in range (len(lista)-1):
        if lista[i] > lista[i+1]:
            ordenada = False
    
    return ordenada
                
    
    
print (lista1)  
print (f"{estaOrdenada(lista1)}")
print()
print(lista2)
print (f"{estaOrdenada(lista2)}")
    
    