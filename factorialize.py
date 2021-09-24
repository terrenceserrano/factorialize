#create a program that will factorialize any input number

from math import *

num = int(input("Input any number here: ")) #this will take any number to be factorialize
print("Factorializing this number: " + str(num))
fac = 1 #this is the start of the count, because the factorial of zero is 1

if num < 0: #this is for the condition if the input is below zero
    print("This number is not factorable")
elif num == 0: #this is for the condition if the input is 1
    print("The factorial of zero is 1")
else:
    #we are using the in keyword so that the i variable name will have a function of range(a, b)
    for i in range(1, num + 1): #we used i as the iteration vairable and in the range function we used 1 as the start and num + 1 as the increment
        fac = fac * i #we used this logic for the factorial from 1 times the iterations
    print("The factorial of the " + str(num) + " is: " + str(fac))



