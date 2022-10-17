

hora1=int(input(" Inserte hora1: "))
min1=int(input(" Inserte min1: "))
seg1=int(input(" Inserte seg1: "))

hora2=int(input(" Inserte hora2: "))
min2=int(input(" Inserte min2: "))
seg2=int(input(" Inserte seg2: "))

if 0<=hora1<24 and 0<=hora2<24 and 0<=min1<59 and 0<=min2<59 and 0<=seg1<59 and 0<=seg2<=59:
    
    if hora1<hora2:
        print("La hora 1 es menor que la hora 2")
    elif hora2<hora1:
            print(" La hora 2 es menor que la hora 1")
    else:
        if min1<min2:
            print("La hora 1 es menor que la hora 2")
        elif min1>min2:
            print(" La hora 2 es menor que la hora 1")
        
        else:
            if seg1<seg2:
                print("La hora 1 es menor que la hora 2")
            elif seg1>seg2:
                print("La hora 2 es menor que la hora 1")
            else:
                print("Las horas son iguales")
else:
    print("Alguna de las horas es incorrecta")