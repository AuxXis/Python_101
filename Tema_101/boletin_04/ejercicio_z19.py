
base = int(input("Introduzca número base: "))
exponente = int(input("Introduzca número exponente: "))

potencia = 1

while exponente<0:
    exponente = int(input("El exponente no puede ser un número negativo: "))
 
for i in range (1, exponente):
    potencia = potencia*base
        
if exponente==0:
    print("El resultado es: 1")
    
    
print(f" {base*potencia}")