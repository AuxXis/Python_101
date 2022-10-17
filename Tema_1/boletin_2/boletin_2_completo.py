#1_ejercicio

#1.a)
print("1.a)")
#sb=sueldoBase
#sn=sueldoBruto
sb=1000
sn=(sb-sb*0.22)
print(sn)

print(sb-sb*0.22==sn)

sb=1000
sn=300
print(sb-sb*0.22==sn)




#1.b
print("1.b)")

dia=-2
valido=dia>=1 and dia <=31
valido2=dia>0 and dia<32
valido3=1<=dia<=31
print(dia>=1 and dia<=31)


dia=1
valido=dia>=1 and dia <=31
valido2=dia>0 and dia<32
valido3=1<=dia<=31
print(dia>0 and dia<32)

dia=31
valido=dia>=1 and dia <=31
valido2=dia>0 and dia<32
valido3=1<=dia<=31
print(dia>=1 and dia <=31)

dia=33
valido=dia>=1 and dia <=31

valido2=dia>0 and dia<32
valido3=1<=dia<=31
print(1<=dia<=31)




#1.c)
print("1.c)")

numero1=12
numero2=27

print(numero1%3==0 and numero2%3==0)

numero1=27628
numero2=4
print(numero1%3==0 and numero2%3==0)

numero1=31
numero2=2
print(numero1%3==0 and numero2%3==0)




#1.d
print("1.d)")
nota=8
print(nota>=5)

nota=5
print(nota>=5)

nota=3
print(nota>=5)




#1.e
print("1.e)")

nota1=8
nota2=4
nota3=7
print((nota1 + nota2 + nota3)>=15)


nota1=8
nota2=4
nota3=7
print((nota1 + nota2 + nota3)>=15)





#ejercicio_2

#2.a)
print("2.a)")
nota1=2
nota2=4
nota3=1
 
print(nota1>=5 and nota2>=5 and nota3>=5)

nota1=5
nota2=9
nota3=6
print(nota1>=5 and nota2>=5 and nota3>=5)

nota1=9
nota2=2
nota3=10

print(nota1>=5 and nota2>=5 and nota3>=5)




#2.b)
print("2.b)")

saldo=3000
descubierto=2
print(saldo>=1000 and descubierto<=5)

saldo=2
descubierto=1
print(saldo>=1000 and descubierto<=5)

saldo=10000000
descubierto=5
print(saldo>=1000 and descubierto<5)






#2.c)
print("2.c)")

asignaturaC=10
asignaturaA=3
print(asignaturaA>=asignaturaC*0.30)

aC=12
aA=6
print(aA>=aC*0.30)

aC=12
aA=3
print(aA>=aC*0.30)

aC=8
aA=1
print(aA>=aC*0.30)







#2.d)
print("2.d")

mes=6
dia=31

mesValido30=((mes==4 or mes==6 or mes==9 or mes==11) and (1<=dia<=30))
mesValido31=((mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==12) and (1<=dia<=31))
mesValido28=(mes==2 and (1<=dia<=28))

print(mesValido30 or mesValido31 or mesValido28)



mes=6
dia=30

mesValido30=((mes==4 or mes==6 or mes==9 or mes==11) and (1<=dia<=30))
mesValido31=((mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==12) and (1<=dia<=31))
mesValido28=(mes==2 and (1<=dia<=28))

print(mesValido30 or mesValido31 or mesValido28)


mes=2
dia=30

mesValido30=((mes==4 or mes==6 or mes==9 or mes==11) and (1<=dia<=30))
mesValido31=((mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==12) and (1<=dia<=31))
mesValido28=(mes==2 and (1<=dia<=28))

print(mesValido30 or mesValido31 or mesValido28)

mes=1
dia=31

mesValido30=((mes==4 or mes==6 or mes==9 or mes==11) and (1<=dia<=30))
mesValido31=((mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==12) and (1<=dia<=31))
mesValido28=(mes==2 and (1<=dia<=28))

print(mesValido30 or mesValido31 or mesValido28)


