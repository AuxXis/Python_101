#a)
print("a)")
cantidad=-1
print(cantidad>=300 or cantidad>0)
print(0<cantidad<=300)
print(not(cantidad<=300 or cantidad<0))


#b)
print("b)")
edad=30
print(edad<16 or edad>22)
edad=18
print(edad<16 or edad>22)


#c)
print("c)")
respuesta="S"
print(respuesta=="S" or respuesta=="N")

respuesta="N"
print(respuesta=="S" or respuesta=="N")

respuesta="X"
print(respuesta=="S" or respuesta=="N")


#d)
print("d)")

numero=21 #false
print(not(numero%7==0 or numero%3==0))

numero=15 #False
print(not(numero%7==0 or numero%3==0))

numero=14 #False
print(not(numero%7==0 or numero%3==0))

numero=16 #True
print(not(numero%7==0 or numero%3==0))

