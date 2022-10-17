
producto= input(" Inserte el tipo de producto: ").upper()
precio= int(input(" Introduzca el precio del producto: "))
producto=("C" or producto=="A" or producto=="B")
if (producto!="C" or producto!="B" or producto!="A"):
    print("El producto no existe.")
elif(producto=="A" or precio<0):
    print(f" El producto {producto} tiene un precio de {precio*0.93}€.")
elif (producto=="C" or precio<500):
    print(f" El producto {producto} tiene un precio de {precio*0.88}€.")
else:
    print(f"El producto {producto} tiene un precio de {precio*0.91}€.")
