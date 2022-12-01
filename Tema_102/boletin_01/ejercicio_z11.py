'''
Escribe una función intersect que reciba dos listas y devuelva otra lista 
con los elementos que son comunes a ambas, sin repetir ninguno.
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

def intersect(list1,list2):
    intersect = []
    for i in range (len(list1)):
        if list1[i] in list2:
            intersect.append(list1[i])
    return intersect


print (intersect(list1,list2))