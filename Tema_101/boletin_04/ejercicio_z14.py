
precio1 = 1
precio2 = 0.8
precio3 = 0.70
precio4 = 0.50


tiempo=float(input("Inserte el tiempo de la llamada en minutos: "))
dia=input("Escriba el día de la semana en que se realizó la llamada: ").lower()
turno=input("Introduzca el turno en el que se realizó la llamada (mañana o tarde): ").lower()

if(dia=="domingo"):
    if(tiempo<=5):
        print(f"Su llamada tiene un coste de {precio1+(precio1*0.97)}€")
    elif(tiempo>5 and tiempo<9):
        print(f"Su llamada tiene un valor de {precio1+precio2+(precio1*0.97)}€")
    elif(tiempo>8 and tiempo<11):
        print(f"Su llamada tiene un valor de {precio1+precio2+precio3+(precio1*0.97)}€")
    elif(tiempo>=10):
        print(f"Su llamada tiene un valor de {precio1+precio2+precio3+(precio1*0.97)}€")
        
if((dia=="lunes" or dia=="martes" or dia=="miercoles" or dia=="jueves" or dia=="viernes" or dia=="sabado") and (turno=="mañana")):
    if(tiempo<=5):
        print(f"Su llamada tiene un coste de {precio1+(precio1*0.85)}€")
    elif(tiempo>5 and tiempo<9):
        print(f"Su llamada tiene un valor de {precio1+precio2+(precio1*0.85)}€")
    elif(tiempo>8 and tiempo<11):
        print(f"Su llamada tiene un valor de {precio1+precio2+precio3+(precio1*0.85)}€")
    elif(tiempo>=10):
        print(f"Su llamada tiene un valor de {precio1+precio2+precio3+(precio1*0.85)}€")
        
if((dia=="lunes" or dia=="martes" or dia=="miercoles" or dia=="jueves" or dia=="viernes" or dia=="sabado") and (turno=="tarde")):
    if(tiempo<=5):
        print(f"Su llamada tiene un coste de {precio1+(precio1*0.90)}€")
    elif(tiempo>5 and tiempo<9):
        print(f"Su llamada tiene un valor de {precio1+precio2+(precio1*0.90)}€")
    elif(tiempo>8 and tiempo<11):
        print(f"Su llamada tiene un valor de {precio1+precio2+precio3+(precio1*0.90)}€")
    elif(tiempo>=10):
        print(f"Su llamada tiene un valor de {precio1+precio2+precio3+(precio1*0.90)}€")
        
else:
    print("¡ERROR! Introduzca valores correctos.")
        