'''
Diseña una función llamada estaOrdenada que reciba una lista de elementos y devuelva True si está ordenada
 o False en caso contrario
 
 '''

lista = [36,493,43,543,754]

def estaOrdenada(lista):
    ordenada = True
    for i in range (len(lista)-1):
        if lista[i] > lista[i+1]:
            ordenada = False
    
    return ordenada
                
    
    
print (lista)  
  
print (f"{estaOrdenada(lista)}")
    
    