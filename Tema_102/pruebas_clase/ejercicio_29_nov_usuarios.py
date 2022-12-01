name = input("Nombre: ")
surname1 = input("Primer apellido: ")
surname2 = input("Segundo apellido: ")
dni = input("DNI: ")


def generar_usuario(name, surname1, surname2, dni):
    user = []
    user = [name [0:3] + surname1 [-3:] + surname2 [0:3] + dni[4:8]]
    return user                     
    
   
print (generar_usuario(name,surname1, surname2, dni))       
print()
print()      

def menu():
    print ("***********************************")
    print ("1. Añadir un usuario válido.")
    print ("2. Eliminar un usuario")
    print ("3. Crear un usuario")
    print ("4. Consultar usuarios.")
    print ("5. Borrar usuarios.")
    print ("6. Salir.")
    
   
  
users_list = ["", "", "", "", ""]
MAXIMO = 5
count = 0

option = input("Seleccione una acción del menu:")


while option!=6:
    
    if option == "1":
        user = input("Añada un usuario válido a la lista: ")
        if count <5:
            users_list.append(user)
        else:
            users_list[count%MAXIMO] = user
            
        count+=1
        
    elif option == "2":
        print (users_list)
        exist = False
        user = input("Introduzca usuario a eliminar: ")
        for i in range (len(users_list)):
            if user == users_list[i]:
                users_list[i] = ""
                exist = True
        if not exist:
            print("El usuario no existe.")
        
    elif option == "3":
        name = input("Nombre: ")
        surname1 = input("Primer apellido: ")
        surname2 = input("Segundo apellido: ")
        dni = input("DNI: ")
        user = generar_usuario(name, surname1, surname2, dni)
        
                
    elif option == "4":
        print (users_list)
        
    elif option =="5":
        lista = []
        lista.clear()
        lista = ["", "", "", "", ""]
    
        
'''
eliminar usuario con remove:

if user in lista:
    lista.remove(user))
else:
    print ("Elusuario no existe.")
'''