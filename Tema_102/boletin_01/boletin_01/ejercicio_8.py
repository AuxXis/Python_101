'''
Realiza un programa que añada números enteros a una lista hasta que se introduzca un número negativo. 
Haciendo uso de esta lista, elabora funciones que devuelvan:
a. una lista con todos los que sean primos.
b. el sumatorio
c. el promedio de los valores.
d. una lista con el factorial de cada uno de esos números.
'''

print("Please enter numbers. Enter a negative number to show the results. ")

number = int(input("Enter a number: "))
lista=[]


while number > 0:
    lista.append (number)
    number = int(input("Enter a number: "))
    

def sumatorio(lista):
    suma = 0
    for i in range (len(lista)):
        suma+=lista[i]
    
    return suma
        
def promedio(lista):
    promedio = sumatorio(lista)/len(lista)
    
    return promedio

print (lista)
print(sumatorio(lista))
print (promedio(lista))