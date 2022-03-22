"""
module docstring
"""


def problem_1():
    """

    :return:
    """
    for i in ['a', 'b', 'c']:
        try:
            print(i ** 2)
        except TypeError:
            print('not integer number')


def problem_2():
    """

    :return:
    """
    x = 5
    y = 0
    try:
        z = x / y
        print(z)
    except ZeroDivisionError:
        print('error division by zero')
    finally:
        print('All Done')


def problem_3():
    """

    :return:
    """
    while True:
        try:
            input_number = int(input('input integer number: '))
        except:
            print('Please input valid integer number \n')
            continue
        else:
            break
    print('Result: {}'.format(input_number ** 2))


if __name__ == '__main__':
    problem_3()
