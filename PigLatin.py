'''
    Pig Latin is a silly made-up language that alters English words. 
    If a word begins with a vowel, the word yay is added to the end of it.
    If a word begins with a consonant or consonant cluster (like ch or gr), 
    that consonant or cluster is moved to the end of the word followed by ay.

    eg: input  = My name is AL SWEIGART and I am 4,000 years old.
        output = Ymay amenay isyay ALYAY EIGARTSWAY andyay Iyay amyay 4,000 yearsyay oldyay.
'''

import re

small_vowels = ['a', 'e', 'i', 'o', 'u']
capital_vowels = ['A', 'E', 'I', 'O', 'U']

print('Enter the English message to translate into Pig Latin:')
message = input()

words = message.strip().split(' ')

updated_message = []

# regex to match numbers with optional commas and decimal points
number_pattern = re.compile(r'^[\d,]+(\.\d+)?$')

for word in words:
    # Skip if it's a number like 4,000 or 1,000.25
    if number_pattern.match(word):
        updated_message.append(word)  # keep the number as-is
        continue

    if word[0] in small_vowels or word[0] in capital_vowels:
        updated_message.append(word + 'yay')
    else:
        # consonant case
        first_letter = word[0]
        new_word = word[1:] + first_letter + 'ay'
        updated_message.append(new_word)

print(' '.join(updated_message))
