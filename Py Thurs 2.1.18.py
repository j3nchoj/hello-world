# Data types

# strings
_str = "test"

#booleans
_bool = True
_bool_false = False

#integer
_int = 1
_int_neg = -1
_float = 2.8

# casting

output = int('1') + 1
output2 = '1' + str(1)
# this will not work, '1' is a string and 1 is a number

print(bool(0))
print(bool(1))
print(bool(.1))
print(bool('false'))
print(bool(None))
print(bool([]))

# list
_list = ['Alex', 'Grande', 'Sarah', 'Jen', 'Laura', 'Justin', 'Danielle']

_list2 = list()

"""
Practice: print each letter in a given string
"""
# for {variable_name} in <collection>:
#   <action>
# Used for lists (Ex: counts = [1,2,3,4,5]
# for count in counts
name = 'name'
for character in name:
    print(character)

"""
Practice: create a function that takes an input,
then prints each character of the input
"""


# DEF is key word to define and remember
def print_charcater(input):
    for charcater in input:
        print(charcater)


print_charcater('purple')

"""
practice: create a function that takes two inputs,
then prints True/False whether or not the first input
is contained within the second input
"""


# == compares
def search_character(search, find):
    for character in find:
        if character == search:
            print(True)
            search_character('a', 'apple')
