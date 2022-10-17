
print("7)")

'''estadoCivil= input("Introduzca su estado civil ( C / V / S / D): ").upper()
edad=int(input(" Introduzca su edad: "))

if (estadoCivil == "C" and edad<35):
    print(" Su estado civil es casado/-a y su porcentaje de retención es un 11.3%.")
elif (estadoCivil == "V" and edad<35):
    print(" Su estado civil es viudo/-a y su porcentaje de retención es un 11.3%.")
elif (estadoCivil == "S" and edad<35):
    print(" Su estado civil es soltero/-a y su porcentaje de rentención es un 12%.")
elif (estadoCivil == "D" and edad<35):
    print(" Su estado civil es divorciado/-a y su porcentaje de retención es un 12%.")
elif (estadoCivil== "C" or estadoCivil=="V" or estadoCivil=="S" or estadoCivil=="D" and edad>50):
    print (f" Su estado civil es {estadoCivil} y su porcentaje de rentención es un 8.5%")
else:
    print(f" Su retención es un 10.5%.")'''
    

#CORRECCIÓN

estadoCivil= input("Introduzca su estado civil ( C / V / S / D): ").upper()
edad=int(input(" Introduzca su edad: "))


if not (estadoCivil != "S" and estadoCivil != "D" and estadoCivil != "C" and estadoCivil != "V"):
    print("Los datos introducidos no son correctos.")
    
    
    if edad < 35 :
        if estadoCivil == "S" or estadoCivil== "D":
            print("Su retención es del 12%.")
        elif estadoCivil == "V" or estadoCivil== "C":
            print("Su rentendión es del 11.3%.")   
      
    elif edad > 50 :
        print("Su retención es del 8.5")
    else:
        print(" Su retención es un 10.5%.")
        
else:
    print ("Los datos son incorrectos.") 

  
        
        