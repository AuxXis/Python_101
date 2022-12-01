'''
Design a program that reads two integer numbers, for example numberA and
numberB, and calculates the product of both numbers without use multiplication, but
using the sum. The messages are the following:
“Enter one number:”
“The product is XX”
'''

numberA = int(input("Enter one number: "))
numberB = int(input("Enter another number: "))
producto=0



   
for i in range (abs(numberA)):
    producto = producto+numberB

if numberA<0:
    producto = -producto
    
print(f"The product is {producto}")

