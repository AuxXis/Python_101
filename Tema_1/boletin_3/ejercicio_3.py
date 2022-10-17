numero= int(input(" Introduce un número: "))

if (numero%2==0 and numero%3==0):
    print(("El numero %s es multiplo de 2 y de 3" %numero))
elif (numero%3==0):
    print((" El número %s es multiplo de 3" %(numero)))
elif (numero%2==0):
    print((" El número %s es múltiplo de 2" %(numero)))