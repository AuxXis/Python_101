'''
Design a program that reads an integer positive number greater than 0 and says if
it’s a “perfect number”. A number is perfect if it is equal to the sum of all its divisors.
The messages are the following:
“Enter an integer positive number greater than 0:”
“The number is not valid, try again.”
“The number is perfect.”
“The number is not perfect
'''

number = int(input("Enter an integer greater than 0: "))

addition=0

while number<=0:
    number = int(input("The number is not valid, try again: "))
                 
for i in range (1, number):
    if number%i==0:
        addition=addition+i

if number==addition:
    print("The number is perfect.")
else:
    print("The number is not perfect.")
