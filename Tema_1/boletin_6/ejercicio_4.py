'''
Design a program that reads a positive number N greater than 0 and show the result
of the sum of the N numbers between 1 and N. If the number N is not valid, the
program should ask for it again. The messages are the following:
“Enter one number greater than 0:”
“The number is not right, try again.”
“The sum of the N first numbers is XX.”
'''


N = int(input("Enter one number greater than 0: "))

for number in range (N):
    print(f"the sum of the N first numbers is {N+number}")
    while N <0:
        N= int(input("The number is not right, try again: "))