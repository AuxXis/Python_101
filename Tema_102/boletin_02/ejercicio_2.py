'''
Design a method called isLeapYear that receives a number and returns False for common years
and True for leap years. You may know that a year is considered to be a leap year if it is divisible by 4,
unless it is also divisible by 100. A year is not a leap year if it is divisible by 100
unless it is also divisible by 400.
'''

year = int(input("Enter a year in order to check whether it is a lap year or not: "))

while not(year > 0):
    year = int(input("Error! Please enter a valid year: "))
    

def isLeapYear(year):   
    if (year % 2 == 0) and (year % 2 == 0):
        leap_year = True        
    else:
        leap_year = False
        
    return leap_year

         
    
    
print(f"Leap year: {isLeapYear(year)}")