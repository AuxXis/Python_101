'''
Escribe una aplicación que pida la fecha actual (día y mes) y el hemisferio
(Norte/Sur) e indique en qué estación se encuentra:
a. Hemisferio Norte: Otoño (desde 23 Septiembre), Invierno (desde 21
diciembre), Primavera (desde 21 Marzo), Verano (desde 21 Junio).
b. Hemisferio Sur: Primavera (desde 23 Septiembre), Verano (desde 21
diciembre), Otoño (desde 21 Marzo), Invierno (desde 21 Junio).
'''




fecha = input("Introduzca una fecha en formato dd-mm-yyyy: ")
hemisferio = input("Introduzca el hemisferio (Norte/Sur): ").upper()


day = int(fecha[0:2])
month = int(fecha[3:5])
year = int(fecha[6:10])


if (month==10 or month==11) or (day<=23<=31 and month==9) or (month == 12 and 1<=day<=21):
    if hemisferio == "NORTE":
        print("Es otoño.")
    elif hemisferio == "SUR":
        print ("Es primavera.")
        
if (month==1 or month==2) or (day<=21<=31 and month==12) or (month == 3 and 1<=day<=21):
    if hemisferio == "NORTE":
        print("Es invierno.")
    elif hemisferio == "SUR":
        print ("Es verano.")
        
if (month==4 or month==5) or (day<=21<=31 and month==3) or (month == 6 and 1<=day<=21):
    if hemisferio == "NORTE":
        print("Es otoño.")
    elif hemisferio == "SUR":
        print ("Es primavera.")
        
if (month==7 or month==8) or (day<=21<=31 and month==3) or (month == 9 and 1<=day<=22):
    if hemisferio == "NORTE":
        print("Es otoño.")
    elif hemisferio == "SUR":
        print ("Es primavera.")