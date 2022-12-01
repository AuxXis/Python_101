'''
Design a method called computeFactorial that receives a positive integer and returns
the factorial for that number. If the number is negative the method should return None.

'''


   
def computer_factorial(num):
    
    while num < 0:
        num = int(input("None"))
    else:
        factorial = 1
        while num > 1:
            factorial = factorial*num
            num = num-1
            
    return factorial

num = int(input(" Enter an integer positive number: "))

print (f"The factorial for this number is: {computer_factorial(num)}")