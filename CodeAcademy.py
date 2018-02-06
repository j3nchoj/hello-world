##functions are a way to reuse a piece of code with a few different values
##Cleaner and can be used repeatedly

# header = def nameoffunction(parameters):
def hello_world():  # there are no parameters
    '''Add a comment to say what the function does'''
    # body describes procedures the function carries out. indent
    print "hello World!"


'''example'''


def spam():
    """this will print Eggs! to screen"""
    print "Eggs!"


def square(n):
    """Returns the square of a number."""
    squared = n ** 2
    print "%d squared is %d." % (n, squared)
    return squared


# Call the square function on line 10! Make sure to
# include the number 10 between the parentheses.

square(10)


# line 26 is an example of calling the function
# N is a parameter of square

def power(base, exponent):  # Add your parameters here!
    result = base ** exponent
    print "%d to the power of %d is %d." % (base, exponent, result)


power(37, 4)  # Add your arguments here!


# functions can call other functions
def one_good_turn(n):
    return n + 1


def deserves_another(n):
    return one_good_turn(n) + 2


###Practice function in function
def cube(number):
    return number * number * number


def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False


##Generic Imports
##Python Module named Math, includes useful functions if you have the correct import keyword
# Ask Python to print sqrt(25) on line 3.
import math

print math.sqrt(25)
# changes
