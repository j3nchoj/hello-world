import sys  # import modules from an outside source

_message = sys.argv[0]

# Data Types
_str = "This is a string"  # a sentence or words in quotes
_str_2 = 'this is a str'

_bool = True  # false
_int = 1
_float = 1.0

# Control Types
if True:
    print('hello world')

# Three quotes lets you have a multi-line string
"""
    practice: print each letter in a given string
"""
message = 'programming 101'
# p
# r
# o
# g
# r
# bruteforce
print("p")
print("r")
print("o")
print("g")
print("r")
print("a")
print("m")
print("m")
print("i")
print("n")
print("g")
print (" ")
print("1")
print("0")
print("1")
print ("----")

# for {variable_name} in <collection>:
#   <action>
# Used for lists (Ex: counts = [1,2,3,4,5]
# for count in counts
for letter in message:
    print (letter)

"""
    practice: print true or false if a letter exists in a given string
"""

search_value = 'e'
message = 'hello world'


def find_letter(search_value):


    if search_value in message:
        print(True)
    else:
        print(False)

find_letter('e')
find_letter('a')
find_letter(1)
find_letter('z')
find_letter('y')
