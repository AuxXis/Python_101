'''persona= numero<100 and numero>0'''

numero=int(input(" Inserte edad: "))
if(numero>=0 and numero<100):
    if(numero>=0 and numero<12):
        print(" Esta persona es niño")
    elif(numero>=13 and numero<17):
        print(" Esta persona es adolescente")
    elif(numero>=18 and numero<29):
        print(" Esta persona es joven")
    elif(numero>=29):
        print(" Esta persona es adulta")
    
    


