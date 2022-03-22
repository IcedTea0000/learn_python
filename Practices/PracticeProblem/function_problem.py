def right_justify(input_string):
    """takes a string named s as a parameter
    and prints the string with enough leading spaces so that the last letter of the string is
    in column 70 of the display"""
    print(' ' * (70 - len(input_string)) + input_string)


def spam():
    print('spam')


def spam2(text):
    print(text)


def do_twice1(input_function):
    """run function twice without passing arguments"""
    input_function()
    input_function()


def do_twice2(input_function, argument):
    """run function twice with param"""
    input_function(argument)
    input_function(argument)


def do_four(input_function, argument):
    """call do_twice2 twice"""
    do_twice2(input_function, argument)
    do_twice2(input_function, argument)


if __name__ == '__main__':
    right_justify('test123456723423423423423423424')

    do_four(spam2, 'spamspam')
    do_twice2(print,'print function')
