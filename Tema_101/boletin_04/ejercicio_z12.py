clasificacion=input("Introduzca la clasificación de la uva (A/B): ").upper()
tamano=int(input("Introduzca el tamaño de la uva (1/2): "))

if(clasificacion=="A" and tamano==1):
    print("Su uva tiene una ganancia de 20cents.")
elif(clasificacion=="A" and tamano==2):
    print("Su uva tiene una ganancia de 30 cents. ")
elif(clasificacion=="B" and tamano==1):
    print("Su uva tiene una rebaja de 30 cents.")
elif(clasificacion== "B" and tamano==2):
    print("Su uva tiene una rebaja de 50 cents.")