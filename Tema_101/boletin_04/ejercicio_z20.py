'''
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el 
segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un programa para determinar 
cuánto debe pagar mensualmente y el total de lo que pagará después de los 20 meses.
'''

cuota=10

for i in range (2,21):
    print(f"El pago del mes {i+1} es {cuota*2}")

    cuota = cuota*2
   
print(f"El total a pagar del artículo es: {i+cuota*2}")

    
    