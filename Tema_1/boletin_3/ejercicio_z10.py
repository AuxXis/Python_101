numero1=int(input("Inserte cifra: "))
operacion=input("Inserte operación: ")
numero2=int(input("Inserte cifra: "))


if(operacion=="+"):
    print("Su resultado es:", numero1+numero2)
elif(operacion=="-"):
    print("Su resultado es: ", numero1-numero2)
elif(operacion=="/"):
    print("Su resultado es: ", numero1/numero2)
elif(operacion=="*"):
    print("Su resultado es: ", numero1*numero2)
else:
    print("¡ERROR!")
    
    
    