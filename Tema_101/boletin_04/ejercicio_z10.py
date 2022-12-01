A=float(input("Introduzca el lado A: "))
B=float(input("Introduzca el lado B: "))
C=float(input("Introduzca el lado C: "))

if(((A**2+B**2)==C**2) or ((A**2+C**2)==B**2) or ((C**2+B**2)==A**2)):
    print("Su triángulo es un triángulo rectángulo.")
elif(A==B and A==C and B==C):
    print("Su triángulo es un triángulo equilátero.")
elif(A==B or A==C or B==C):
    print("Su triángulo es un triángulo isósceles.")
else:
    print("Su triángulo es un triángulo escaleno. ")

