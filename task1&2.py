# Functions and modules in python
n = int(input("Enter a number: "))

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * (factorial(n-1))

result = factorial(10)
print("Factorial of 10 is: ", result)


#Task 2: Using the Math Module for Calculations

n = int(input("Enter a number: "))

import math

result = math.sqrt(n)
print("square root: ", result)

result = math.log(n)
print("logarithm: ", result)

result = math.sin(n)
print("sine: ", result)



