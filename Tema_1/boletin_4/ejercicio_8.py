euro2=(float(input("Introduzca las monedas de 2€ que tiene: ")))
euro1=(float(input("Introduzca las monedas de 1€ que tiene: ")))
centimo50=(float(input("Introduzca las monedas de 50cent que tiene: ")))
centimo20=(float(input("Introduzca las monedas de 20cent que tiene: ")))
centimo10=(float(input("Introduzca las monedas de 10cent que tiene: ")))

Totalcentimos=((euro2*200) + (euro1*100) + ((centimo50*50) + (centimo20*20) + (centimo10*10)))

print(f"Usted tiene un total de: {Totalcentimos//100}Euros y {Totalcentimos%100} céntimos")