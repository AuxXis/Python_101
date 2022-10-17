alumnos=int(input("Introduzca el número de alumnos: "))

if(alumnos>=100):
    print(f"Se debe cobrarun total de {(4000/alumnos)+65}€")
if(49<alumnos<100):
    print(f"Se debe cobrarun total de {(4000/alumnos)+70}€")
if(29<alumnos<50):
    print(f"Se debe cobrarun total de {(4000/alumnos)+95}€")
if(alumnos<30):
    print(f"Se debe cobrarun total de {4000/alumnos}€")