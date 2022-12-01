'''
Design a program for reading an integer between 0 and 10 and show the times table.
To ask for the number you should show the next message "Enter one number
between 0 and 10”. If the number is out of the boundaries, the program should show
the message “The number is out of the boundaries”. If the number is valid, it should
show the times table following the next format:
7*0=0
7*1=7
…..
7*10=70
'''


factor = int(input("Enter one number between 0 and 10: "))
  
    
if (factor>0 and factor<10):
        for number in range (11):
            print(f"{factor} * {number} == {factor*number}")
else:
    print("The number is out of the boundaries.")