'''
4. Crea un programa que lea por teclado números de forma sucesiva y los guarde en una lista; 
el proceso de lectura y guardado finalizará cuando metamos un número negativo. En ese momento
 se mostrará el elemento mayor y los números pares.
'''

print("Please enter numbers. Enter a negative number to show the results: ")

number = int(input("Enter a number: "))
lista=[]


while number > 0:
    lista.append (number)
    number = int(input("Enter a number: "))
    
    
def numero_mayor():
    mayor = lista[0]
    for i in range (len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    return mayor



def numero_menor():
    menor = lista[0]
    for i in range (len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    return menor

def lista_pares(lista):
    lista_par=[]  
    for i in lista:
        if i % 2 == 0:
            lista_par.append(i)
    return lista_par


        
print(f"Number list: {lista}")

print(f"Highest number: {numero_mayor()}")
print(f"Lowest number: {numero_menor()}")
print(f"Even numbers: {lista_pares(lista)}")