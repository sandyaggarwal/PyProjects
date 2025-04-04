import random

upper_char = ['A','B','C','D','E','F']

lower_char = ['a','b','c','d','e','f','g','h']

num_set = [1,2,3,4,5,6,7,8,9,0]

special_set = ['~','|','@','#',"$","%","^","*"]

password = f'{random.choice(upper_char)}{random.choice(lower_char)}{random.choice(num_set)}{random.choice(special_set)}{random.choice(upper_char)}{random.choice(lower_char)}{random.choice(num_set)}{random.choice(special_set)}'

print(f'This is random genrated password {password}')
