'''
    Program to convert the lines in to bullet points on clipboard 
'''


import pyperclip

text = pyperclip.paste()
bullet_list = text.strip().split('\n')

'''
    list is mutable object, we will traverse through 
    the list using index and will modify this list instead 
    of printing directly.
'''
for index in range(len(bullet_list)):
    bullet_list[index] = f'* {bullet_list[index]}'

text = '\n'.join(bullet_list)
pyperclip.copy(text)