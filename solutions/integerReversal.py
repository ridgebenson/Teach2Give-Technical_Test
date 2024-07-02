# Question 1
# Design a function that reverses the digits of an integer.
# For example, 50 should become 5 and -12 should become -21.

def reverse_integer(num):
    if num < 0:
        sign = -1
    else:
        sign = 1
    reversed_num = int(str(abs(num))[::-1])
    return sign * reversed_num


print(reverse_integer(50))
print(reverse_integer(-12))
