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
    if len(list1)>len(list2):
        for i in range (len(list1)):
            if list1[i]==list2[i]:
                intersect.append(list1[i])
    
    else:
        for i in range (len(list2)):
            if list1[i]==list2[i]:
                intersect.append(list2[i])


print (intersect(list1,list2))