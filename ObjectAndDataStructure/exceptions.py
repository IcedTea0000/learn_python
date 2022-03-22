def test_exception():
    try:
        result = 10 + 20
        print(result)
    except:
        print('error occurred')
    else:
        print('no error')
        return
    finally:
        print('i always run')
    print('after try except block')


def test_exception2():
    try:
        result = int(input('Provide phone number: '))
    except:
        print('not a number')
    finally:
        print('finally block')
        print('result value: {}'.format(result))
    print('outside of try/except block')


if __name__ == '__main__':
    # test_exception()
    test_exception2()