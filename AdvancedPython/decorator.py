def hello(name='Martin'):
    print('hello() function has been executed')

    def greet():
        return '\t greet() function'

    def welcome():
        return '\t welcome() function'

    print('I will return a function based on parameter')
    if name == 'Martin':
        return welcome()
    else:
        return greet()


def other(some_func):
    print('Other code runs here')
    print(some_func())


def new_decorator(original_func):
    def wrap_func():
        print('some extra code, before original function')
        original_func()
        print('some extra code, after original function')

    return wrap_func()


# @new_decorator
@new_decorator
def func_needs_decorator():
    print('function that needs to add decorator')
    pass


if __name__ == '__main__':
    # print(hello())
    # decorated_function = new_decorator(func_needs_decorator)
    func_needs_decorator