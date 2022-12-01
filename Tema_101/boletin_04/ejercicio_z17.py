
Numero1 = int(input("Introduzca un número: "))
Numero2 = int(input("Introduzca un número: "))

if Numero1>Numero2:
        tmp=Numero2
        Numero2=Numero1
        Numero1=tmp
for i in range (Numero1, Numero2):
    if (i%2==0):
        print(f"{i}")
    
    
