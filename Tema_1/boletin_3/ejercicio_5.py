numero1=int(input(" Interte primer número: "))
numero2=int(input(" Inserte segundo número: "))
numero3=int(input(" Inserte tercer número: "))
numero4=int(input(" Inserte cuarto número: "))
media=(numero1+numero2+numero3+numero4)/4
print(" La media es %s " %(media))
if(numero1>media):
    print(" El primer número: %s es mayor que la media" %(numero1))
if(numero2>media):
    print(" El segundo número: %s es mayor que la media" %(numero2))
if(numero3>media):
    print(" El tercer número: %s es mayor que la media" %(numero3))
if(numero4>media):
    print("El cuarto número: %s es mayor que la media" %(numero4))