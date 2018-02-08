# DataTypes
_str = "this is a string"
_bool = True or False
_int = 3
_list = [1, 2, 3, 4, 5]
_dict = "dictionary"

# Casting
# str = int = runtime exeption
print ('1' + str(1))  # this will not work, cant add string and integer - add str()
#
# #CONTROL STRUCTURES
# # --for loops--
# # for {variable_name} in <collection> (<- string):
# #     <action>
name = 'Justin'

for character in name:
    print(character)

# # --Logical--
# # if <bool>:
# #    Pass
# # elif <bool>:
# #     Pass
# # else <bool>:
# #     Pass
name = "Jen"
if name == 'Justin':
    print ('1')
elif name == 'Alex':
    print ('2')
elif name == 'Jen':
    print ('3')
elif name == 'Laura':
    print ('4')
else:
    print ('5')
# Can only have one if, one else, many elif. Dont need else or elif.

# # -- Assignment --
# # =

# # --Comparisions--
# # == ->equals
# # != -> not equals
# # > greater then
# # >= greater then or equal to

'''
Practice: create a function that takes an input,
then prints each character of the input
'''


def print_characters(input_string):
    for characters in input_string:
        print(character)


'''
Practice: creat a function that takes two inputs,
then prints True/False whetehr or not the first input
is contained within the second input
'''

text_value = 'some input'


def search_string(search_value, input_string):
    for character in input_string:
        if search_value == character:
            print(True)


# implement function here

text_value = 'some input'  # we're searching this string, can change 'some input'

def search_string(search, text_input):
    result = False  #assuming its False. If delete for loop, everything is False in result
    for character in text_input:
        if character == search:
            result = True
    print(result)


search_string('a', text_value)  # false
search_string('s', text_value)  # true
search_string('S', text_value)  # false
search_string('T', text_value)  # false
