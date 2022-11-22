
'''
'3. Realiza un programa que solicite la fecha como tres datos numéricos (día, mes y año) y
 muestre a continuación la fecha en formato largo.
Introduce el día de la fecha: 15
Introduce el mes de a fecha: 3
Introduce el año de a fecha: 2009
La fecha en formato largo es 15 de Marzo de 2009
Debe validar los datos y ejecutarse hasta que se introduzca un día negativo.
'''



def esBisiesto(year):
    return year%4==0 and (year%100!=0 or year%400==0)

def esFechaValida(dd, mm, yyyy):
    maxDay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    fechaValida =  1 <= mm <= 12 and ((1<= dd <= maxDay [mm-1]) or (esBisiesto(yyyy) and 1 <= dd <= 29 and mm == 2))
    return fechaValida

def transformarFormatoLargo(dd, mm, yyyy):
    months = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    
    if esFechaValida(dd, mm, yyyy):
        mensaje = f"{dd} de {months[mm-1]} de {yyyy}"
    
    else:
        mensaje="La fecha no es validad."
    
    return (mensaje)

day = int(input("Introduce el día: "))
month = int(input("Introduce el mes: "))
year = int(input("Introduce el año: "))
print(transformarFormatoLargo(day, month, year ))

while day >= 0:
    day = int(input("Introduce el día: "))
    month = int(input("Introduce el mes: "))
    year = int(input("Introduce el año: "))
    print(transformarFormatoLargo(day, month, year))