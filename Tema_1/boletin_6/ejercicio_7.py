'''7. Design a program that asks how many numbers the user wants to write. After the
user enters all numbers, the program should say the medium of the numbers. If the
user inputs a wrong number, the program should ask for it again. The messages are
the following:
“How many numbers do you want input?” to ask for the number of numbers.
“Enter one number greater than 0:” to ask for a number.
“The number is not valid, it should be greater than 0” to inform that the number is not
valid.
“The medium is XX.XX” to show the result.
'''

cantidad = int (input("How many numbers do you want to input? "))

while cantidad <= 0:
    cantidad = int (input("How many numbers do you want to input? "))

total, contador = 0, 0  

while cantidad > contador:
    numero = int(input("Enter one number greater than 0: "))
    while numero <=0:
        numero = int(input("The number is not valid, it should be greater than 0. Enter one number greater than 0."))
    contador += 1
    total += numero
    
    
print(f"The medium is {total/cantidad}.")