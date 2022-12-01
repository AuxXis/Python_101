'''
Design a method called powerIt that receives two integers and raises the first number to the second.
You may use the product or recursion and check the values. If no exponent is provided
the first number is raised to 0.
'''

base = int(input("Enter a number to be raised: "))
exponent = int(input("Enter a number to raise: "))

def powerIt():
    power = 0
    while exponent > 0:
        
        