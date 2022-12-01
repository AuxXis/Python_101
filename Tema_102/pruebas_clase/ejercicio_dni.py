'''
num=15409737%23
print (num)
'''

num = int(input("Introduzca numeros del DNI: "))

def asignar_letra(num):  
    letra = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
    for i in range (len(letra)):
        if num%23 == letra[i]:
            letra = letra[i]
        
    return letra
          
    
print (asignar_letra(num))