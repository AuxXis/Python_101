''' 8.0
Design a program that asks for a set of numbers. After inputting each number, the
program should ask “Do you want to enter more numbers (Y/N)?”. If the answer is “Y”
the program asks for other numbers. When the user finishes to enter all the numbers,
the program should say which one is the smallest. The messages are the following:
“Enter one number:”
“Do you want to enter more number (Y/N)?”
“The smallest number is XX”
'''

int(input("Enter one number: "))

query = input("Do you want to enter more numbers (Y/N): ").upper()
if not(query=="Y" and query=="N"):
    print("Please enter a valid number (Y/N): ")
    
while query == "Y" and (query!="N"):
    int(input("Enter one number: "))
    query= input("Do you want to enter more numbers (Y/N): ").upper()
    
    
    

