'''
Design a program to show all numbers between 1 and 100. If the number is a
multiple of 7 you should show the message "The number xx is a multiple of 7". If the
number is a multiple of 13 you should show the message "The number xx is a
multiple of 13". If the number is a multiple of 7 and 13 you should show both
messages.
'''

for number in range (101):
    print(number)
    if (number%7==0 and number%13==0):
        print (f"The number {number} is a multiple of 7 and 13.") 
    elif number%13==0:
        print (f"The number {number} is a multiple of 13.")
    elif number%7==0:
        print (f"The number {number} is a multiple of 7.")