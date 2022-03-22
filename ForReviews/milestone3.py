# ==============================================================================================
# def hello():
#     return "hello"
#
# greet = hello
# print(greet())


# def hello():
#     print("hello() function executed")
#
#     def greet():
#         return "greeting"
#
#     def welcome():
#         return "welcome"
#
# def a_function(some_other_func):
#     print("a_function() executed")
#     some_other_func()
#
# a_function(hello)


# def a_decorator(original_func):
#     def wrap_func():
#         print("extra code before original function")
#         original_func()
#         print("extra code after original function")
#
#     return wrap_func
#
# @a_decorator
# def func_needs_decorator():
#     print("function need decorator")

# decorated_func = a_decorator(func_needs_decorator)
# decorated_func()
# func_needs_decorator()
# ==============================================================================================
# def gen_cubes(num):
#     for x in range(num):
#         yield x ** 3


# for y in gen_cubes(100):
#     print(y)

# generator1 = gen_cubes(3)
# print(generator1)
# print(next(generator1))
# print(next(generator1))
# print(next(generator1))
# print(next(generator1))

# ==============================================================================================
# def gen_square(number):
#     for num in range(number):
#         yield num ** 2
#
# gen1 = gen_square(100)
# for x in gen1:
#     print(x)
