x1=int(input("Inserte x1: "))
y1=int(input("Inserte y1: "))
punto= x1-y1

x2=int(input("Inserte x2:"))
y2=int(input("Inserte y2:"))
punto2= x2-y2


print(f"La distancia entre el punto1 y el punto2 es: {((x2-x1)**2 + (y2-y1)**2)**(1/2)}")