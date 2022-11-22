'''
 Crea un programa que genere 100 números de forma aleatoria y que posteriormente
ofrezca al usuario la posibilidad de:
a. Conocer el mayor
b. Conocer el menor
c. Obtener la suma de todos los números
d. Obtener la media
e. Sustituir el valor de un elemento por otro número introducido por teclado
f. Mostrar todos los números
⇒ Realiza cada una de las opciones con funciones.
⇒ Utiliza la función siguiente para generar números aleatorios (entre 0 y 1000).
'''


from random import randint




def lista_aleatoria():
    numero = []
    for i in range (100):
        numero.append(randint(0,1000))
    return numero

lista = lista_aleatoria()


def conocer_mayor(lista):
    mayor = lista[0]
    for i in range (len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    return mayor

def conocer_menor(lista):
    menor = lista[0]
    for i in range (len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    return menor

def suma_elementos_lista(lista):
    suma = 0
    for i in range (len(lista)):
        suma+=lista[i]
    return suma

def obtener_media(lista):
    media = suma_elementos_lista(lista)/1000
    
    return media




def menu ():
    print("**************************+***************************+*******")
    print("a. Conocer el mayor.")
    print("b. Conocer el menor.")
    print("c. Obtener la suma de todos los números.")
    print("d. Obtener la media.")
    print("e. Sustituir el valor de un elemento por otro número introducido por teclado.")
    print("f. Mostrar todos los números.")
    print("**************************+******************************+****")
    
print(f"Tus números aleatorios son: {lista_aleatoria()}")
lista = lista_aleatoria()     
       
       
menu()
opcion = ("a") or ("b") or ("c") or ("d") or ("e") or ("f")
while (opcion == "a") or (opcion == "b") or (opcion == "c") or (opcion == "d") or (opcion == "e") or (opcion == "f"):
    opcion = input("¿Qué quieres hacer con estos números? (Selecciona a/b/c/d/e/f)").lower()

    if opcion == ("a"):  
        print(f"El mayor es: {conocer_mayor(lista)}")
    elif opcion == ("b"):
        print (f"El menor es:{conocer_menor(lista)}")
    elif opcion == ("c"):
        print (f"La suma de todos los numeros es: {suma_elementos_lista(lista)}")
    elif opcion == ("d"):
        print (f"La media de tus números es: {obtener_media(lista)}")
    elif opcion == ("e"):
        print ("Función no disponible") #No he sido capaz de sacar esta opción porque no termino de comprender la forma de orientarlo al cliente.
    elif opcion == ("f"):
        print (f"{lista}")
else:
    print("Opción incorrecta, saliendo del programa.")
              
    

        


