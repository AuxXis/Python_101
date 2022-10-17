'''
En el gimnasio Jacafitness tienen el siguiente horario: Los Lunes, Miércoles y Viernes imparten Spinning 
de 12 a 14, Yoga de 16 a 20 y Body combat de 20 a 22; Los Martes y Jueves La sesión de Spinning y Yoga se intercambian.

Elabora un programa que dé la bienvenida al gimnasio Jacafitness y tras preguntar por la hora 

y el día de la semana te indique la actividad que puedes realizar.
'''

print("Bienvenida/-o al gimnasio Jacafitness" )
hora=float(input("¿Qué hora es? "))
dia=input("¿Qué día de la semana es? ").upper()



if ((dia== "LUNES" or dia=="MIERCOLES" or dia=="VIERNES") and (12<=hora<14)):
    print( "Ahora mismo usted puede asistir a nuestra sesión de Spinning.")
elif ((dia=="LUNES" or dia=="MIERCOLES" or dia=="VIERNES") and (20<=hora<22)):
    print("Ahora mismo usted puede asistir a nuestra sesión de Body combat.")
elif ((dia=="LUNES" or dia=="MIERCOLES" or dia=="VIERNES")  and (16<=hora<20)):
    print("Ahora mismo usted puede asistir a nuestra sesión de yoga.")
elif ((dia=="MARTES" or dia=="JUEVES") and (12<=hora<14)):
    print("Ahora mismo usted puede asistir a nuestra sesión de yoga." )
elif ((dia=="MARTES" or dia=="JUEVES") and (16<=hora<20)):
    print("Ahora mismo usted puede asistir a nuestra sesión de Spining." )
elif ((dia=="MARTES" or dia=="JUEVES") and (20<=hora<22)):
    print("Ahora mismo usted puede asistir a nuestra sesión de Body combat.")
else:
    print("Ahora mismo no hay sesiones.")

