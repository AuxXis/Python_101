'''
5. Design a program that asks for numbers until the user inputs a negative one. When
this happens, the program will show how many positive numbers have been
introduced by the user. The messages are the following:
“Enter a number (negative to finish):”
“You have entered XX positive numbers.”
'''


number = int(input("Enter a number (negative to finish): "))

contador=0
while number > 0:
    number = int(input("Enter a number (negative to finish): "))
    contador = contador+1
   
             
print(f"You have entered {contador} positive numbers.")