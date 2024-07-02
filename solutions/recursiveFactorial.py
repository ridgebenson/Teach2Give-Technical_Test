# Question 2
# Write a recursive function to calculate the factorial of a number
# Recursive Factorial Calculation

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(5))