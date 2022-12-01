'''
Juan recibe dos tipos de regalos de cumpleaños según el año en el que esté: si el
año es impar su familia le regala un puzzle; si es par, recibe dinero.
Cada nuevo cumpleaños recibe más regalos: así, cada año que recibe puzzles
obtiene el doble que el anterior; sin embargo, si se trata de dinero recibe 15€ más
que en la anterior ocasión.
Elabora un programa que calcule cuántos regalos ha recibido en total Juan, para una
edad determinada sabiendo que en el primer cumpleaños le regalaron un puzzle y
en el segundo 20€.
'''
#even = +15€
#odd = *2puzz

puzzlist=1
puzzcount=0
moneycount=0
moneystart=20

year = int(input("Introduzca el cumpleaños:"))

for i in range (1, year+1):
    if i%2!=0:
        puzzcount = puzzlist + (puzzcount*2)   
        moneycount=moneycount
    
    elif year==1:
        moneycount = moneycount
               
    else:
        moneycount = moneycount + moneystart +15
        
           
         
print(f"Juan tiene {puzzcount} puzzles")
print(f"Juan tiene {moneycount}€")