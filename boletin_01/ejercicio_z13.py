'''
Escribe una función que, dada una lista de nombres y una letra, devuelva una lista
con todos los nombres que empiezan por dicha letra. Debe validar los datos.
'''

name_list=["Luisa", "Sara", "Ana", "Lola", "Lucas", "Juan", "Pablo", "Rita" ]
name_letter="L"


def start_list(list, letter):
    start_list = []
    for i in range (len(list)):
        if list[i][0] == letter:
            start_list.append(list[i])
    return start_list


print (start_list(name_list, name_letter))