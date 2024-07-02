# Question 3
# Design a function that takes a string or sequence of characters as input and returns
# the character that appears most frequently.
# Eg 11189 => '1'
# hello => l

def most_frequent_character(s):
    from collections import Counter
    count = Counter(s)
    return count.most_common(1)[0][0]


print(most_frequent_character('11189'))
print(most_frequent_character('hello'))
