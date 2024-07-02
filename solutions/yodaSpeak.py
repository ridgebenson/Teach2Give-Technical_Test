# Question 6
# Master Yoda, a renowned Jedi Master from the Star Wars universe,
# is known for his unique way of speaking. He often reverses the order of words in his sentences.
# For example, instead of saying "I am home" he might say "Home am I".
# Design a function that takes a sentence as input and returns a new sentence with the words reversed
# in the same order that Master Yoda would use.

def reverse_sentence(s):
    return ' '.join(s.split()[::-1])


print(reverse_sentence('I am home'))
print(reverse_sentence('Home am I'))
print(reverse_sentence('Hello, world!'))
print(reverse_sentence('The quick brown fox jumps over the lazy dog'))