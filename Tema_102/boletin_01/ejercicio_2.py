'''
Realiza un programa que lea 10 números, los imprima separados por coma y a
continuación los desplace una posición (y los muestre por pantalla desplazados), de
tal forma que el último pase a la primera posición, el primero a la segunda, el
segundo a la tercera, y así sucesivamente.
Opcional: Añade un parámetro (D/I) a la función para que el controle el sentido del
desplazamiento (a derechas/izquierdas) y otro que indique el número de posiciones
a desplazar (0: quedaría igual, 1: desplaza una posición, etc.).
'''


from random import randint


def random_list():
    numbers = []
    for i in range (20):
        numbers.append(randint(0,20))
        
    return numbers


print (random_list())
list = random_list()

def move_number(list):
    write=list[0]
    keep=0
    for i in range(len(list)):
        
        keep = list[(i+1) % len(list)]
        list[(i+1) % len(list)] = write
        write = keep
    return list

print(move_number(list))