año=int(input("Introduce el año: "))

if(año%4 == 0):
    if(año%100 == 0):
        if(año%400 == 0):
            print("El año introducido es bisiesto.")
        else:
            print("El año introducido no es bisiesto.")
    else:
        print("El año es bisiesto.")
     
else:
    print("El año introducido no es bisiesto.")