# Question 4
# Design a function that determines whether a given string is a pangram.
# A pangram is a sentence or a phrase containing every letter of the alphabet at least once.
# Punctuation anc case are typically ignored.
# For example, the string "The quick brown fox jumps over the lazy dog" is a pangram,
# while "Hello, world!" is not.

def is_pangram(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    for char in alphabet:
        if char not in s:
            return False
    return True


print(is_pangram('The quick brown fox jumps over the lazy dog'))
print(is_pangram('Hello, world!'))
