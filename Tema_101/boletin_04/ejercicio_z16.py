mes=input("Introduzca su mes del año (1-12): ")

if(mes=="4" or mes=="6" or mes=="9" or mes=="11"):
    print("Su mes tiene 30 días.")
elif(mes=="1" or mes=="3" or mes=="5" or mes=="7" or mes=="8" or mes=="12"):
    print("Su mes tiene 31 días.")
elif(mes=="2"):
    print("Su mes tiene 28 días (si no es bisiesto).")
    
else:
    print("¡Introduzca un mes válido!")
