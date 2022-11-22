'''
Escribe una función unionListas que reciba dos listas y devuelva los elementos que pertenecen a una, 
o bien, a la otra, pero sin repetir ninguno (unión de conjuntos).
'''

from random import randint

list1 = []
list2 =[]

def random_list():
    numbers = []
    for i in range (20):
        numbers.append(randint(0,20))
        
    return numbers

list1 = random_list()
list2 = random_list()

print(list1)
print(list2)


def join_lists(list1, list2):
    join=[]
    for i in range(len(list1)):
        if list1[i]!=list2[i]:
            join.append(list1[i])
            join.append(list2[i])
    
    return join

print(join_lists(list1, list2))