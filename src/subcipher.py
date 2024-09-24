"""
--------------------------
Homework 06: Substitution Cipher
--------------------------
STUDENT: UPDATE
SEMESTER: UPDATE
"""
import sys
from string import digits, ascii_letters
from random import sample

ALL_LETTERS_DIGITS = digits + ascii_letters
# use this random key if none is provided, try printing it out to see what it is
RANDOM_KEY = "".join(sample(list(ALL_LETTERS_DIGITS), len(ALL_LETTERS_DIGITS)))


# add your functions here. you should think about how you break up your program. 


def main(action, msg, key):
    """ Starting point of your program. You must start here."""
    ... # same as pass, remove this line when you add your code


# The following allows us to run various features from the command line
# do not modify.
# If you wish to run the program from the command line
# You could do the following
# python3 subcipher.py "Aloha, World"
# that will encrypt this is my message and return both message and key
# you can decrypt by adding -d or --decrypt as the first argument, and then a key after the message
# python3 subcipher.py -d "9HUqv, VUEHQ" "0XkDwIrGzYv17QfNiqgbZHJ5UhKEljCTRnxA9uaySWopM6emc2dP4sL83BVtFO"
# reminder, windows replaces python3 with python
if __name__ == "__main__":
    # check to see if there are command line arguments
    _action = 'encrypt'
    _msg = ''
    _key = ''
    if len(sys.argv) > 1:
        if sys.argv[1] == '-d' or sys.argv[1] == '--decrypt':
            _action = 'decrypt'
            remainder = sys.argv[2:]
        else:
            remainder = sys.argv[1:]
        if len(remainder) > 0:
            _msg = remainder[0]
            if len(remainder) > 1:
                _key = remainder[1]
    main(_action, _msg, _key)
