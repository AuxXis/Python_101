'''
Desarrolla un programa que a partir de una lista de números y pedir un entero k, realice la llamada a tres 
funciones: 
a) para devolver una lista de números con los menores de k. 
b) otra con los mayores que k.
c) otra con aquellos que son múltiplos de k.
'''


from random import randint
new_list = []

def random_list():
    numbers = []
    for i in range (20):
        numbers.append(randint(0,20))
        
    return numbers

new_list = random_list()



def less_than_k(new_list,k):
    minor_list=[]
    for i in new_list:
        if i < k:
            minor_list.append(i)
        
    return minor_list


def greater_than_k(new_list,k):
    greater_list=[]
    for i in new_list:
        if i > k:
            greater_list.append(i)
        
    return greater_list

def multiple_of_k(new_list,k):
    multiple = []
    for i in new_list:
        if i%k == 0:
            multiple.append(i)
        
    return multiple


print("Your list is: ")
print (new_list)
k = int(input("Enter an integer number in order to proceed: "))
print("************************************************************************************************")
print(f"Minor than k: {less_than_k(new_list,k)}")
print(f"Greater than k: {greater_than_k(new_list,k)}")
print(f"Multiples of k: {multiple_of_k(new_list,k)}")


