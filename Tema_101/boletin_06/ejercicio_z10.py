'''
 Design a program that reads an integer positive number and says the “factorial” of
the number. To calculate the factorial you should know that
FACT(0)= 1
FACT(1) =1
FACT(N)= N*(N-1)*(N-2)*....1
The messages are the following:
“Enter an integer positive number:”
“The number is not valid, try again.”
“The factorial is XX”
'''

numero = int(input(" Enter an integer positive number: "))
factorial = 1

while numero < 0:
    numero = int(input(" The number is not valid, try again: "))

for i in range (1, numero+1):
    factorial = factorial*i
   
print(f" The factorial is {factorial}")

