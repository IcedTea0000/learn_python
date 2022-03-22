# def print_all():
#     print('hello')
#     print('today')
#
#
# print_all()
#
# test_var = 2
# test_var2=test_var
# test_var = 'hi'
#
# print(test_var2)
#
# test_str = "hello john doe"
# print(test_str[0])
# print(test_str[-1])
# print(test_str[0:-1:2])
# print(test_str[0:])
# print(test_str[:5])
# print(test_str[2:])
# print(test_str[::1])
#
#
# test_str2 = "heello \nworld"
# print(test_str2)
#
#
# test_str3 = 'Hello World'
# print(test_str3.lower())
# print(test_str3.upper())
# print(test_str3.split())
# print(test_str3.split("l"))
#
# print("string {}".format("INSERTED"))
# print("Hello {} {} {}".format("this", "is", "John"))
# print("Hello {1} {0} {2}".format("this", "is", "John"))
#
#
# list1 = [1,"John",5.6]
# print(len(list1))
# list1[0] = "one"
# print(list1)
# list1.append("appended")
# print(list1)
# print(list1.pop())
# print(list1)
#
# list2 = [1,3,-1,6,-45]
# list2.sort()
# print(list2)
#
# dict1 = {"k1":"v1", "k2":"v2", "k3":"v3"}
# dict2 = {"k1": 123, "k2": [0,1,2], "k3":{"insideKey":100}}
# print(dict2["k2"][1])
# print(dict2.keys())
# print(dict2.values())
# print(dict2.items())
#
# tuple1 = (1,2,3)
# print(tuple1)
#
# set1 ={1,2,3,4,1,1,1}
# set1.add(1)
# print(set1)
#
# print(1>2)
# var1 = None
#
# myFile = open("C:\\test.txt")
# print(myFile.read())
# print(myFile.readlines())
# myFile.close()
#
# with open("C:\\test.txt", mode = "r") as my_open_file:
#     contents = my_open_file.read()
#     # print(contents)
# print(contents)
#
# var1= 0
# if False:
#     print("false")
# elif True:
#     print("true")
#
#
# list1 = [1,2,3,4,5,5]
# for item in list1:
#     print(item+1)
#
# dict1 = {"k1":"v1", "k2":"v2"}
# for item in dict1.items():
#     print(item[1])
#
# list1 = [1,23,1,1,3,5,3,5,7]
# while len(list1) != 0:
#     list1.pop()
#     print(list1)
# else:
#     print("list empty")
#
# list1=[1,2,3,4,5,7]
# for num in range(len(list1)):
#     print(num)
#
# list1=[1,2,3,4,5,7]
# for item in enumerate(list1):
#     print(item)
#
# list1 =[1,2,3,4]
# list2 = ["a","b","c"]
# list3 = ["j"]
# for item in zip(list1, list2, list3):
#     print(item)
#
# from random import shuffle
# list1 = [1,2,3,4,5,6,7,8,9,10]
# shuffle(list1)
# print(list1)
#
# list1 = [item for item in "John Doe"]
# print(list1)
#
# list2 = [num**3 for num in range(1,50) if num%2 == 0]
# print(list2)
# list3 = [num if num%2 == 0 else "ODD" for num in range(1,50)]
# print(list3)
#
#
# def test_function(name):
#     print("Hello "+ name)
# test_function("John")
#
#
# def say_hello(name = "John Doe"):
#     print(f"hello {name}")
#
# say_hello()
# say_hello("Lam")
#
# def add_num(num1, num2):
#     return num1 + num2
#
#
# print(add_num(1, 5))
#
#
# def employee_check(work_hours):
#     max_hour = 0
#     employee_of_month = ""
#
#     for employee, hours in work_hours:
#         if hours > max_hour:
#             max_hour= hours
#             employee_of_month = employee
#         else:
#             pass
#     return employee_of_month, max_hour
#
# work_hours = [("Bill", 5000), ("Jon", 6000), ("Tiara", 3000)]
# result = employee_check(work_hours)
# employee, hour = employee_check(work_hours)
# print(result)
# print(employee)
#
#
# def nested_func():
#     return 1
#
# def outer_func(nested_func):
#     print(nested_func)
#
# outer_func(nested_func())
#
#
# def player_guess():
#     guess = ""
#     while guess not in ["0", "1", "2"]:
#         guess = input("Pick a number: 0, 1, 2 \n")
#     return int(guess)
#
#
# def check_guess(mylist, guess):
#     if mylist[guess] == 'o':
#         print("Correct!")
#     else:
#         print("Wrong guess")
#
#
# from random import shuffle
#
# list1 = ["u", "o", "i"]
# shuffle(list1)
# check_guess(list1, player_guess())
#
# def myFunc(a,b,c=0,d=0,e=0):
#     # return 5% of sum of a and b
#     return sum(a,b,c,d,e)
#
# def myFunc2(*args):
#     print(args)
#     for item in args:
#         print(item)
#     return sum(args)
#
# myFunc2(1,2,3,4,5,6,7)
#
#
# def myFunc3(**kwargs):
#     print(kwargs)
#     if kwargs is None:
#         return
#     for item in kwargs.items():
#         print(item)
#
# myFunc3(k1 = "apple", k2 = "orange")
#
# def myFunc4(*args, **kwargs):
#     print(args)
#     print(kwargs)
# myFunc4(1,2,3,4,5,k1="hi", k2 = "hello")
#
#
# def myfunc(input):
#     temp_list = list(input)
#     for index in range(len(input)-1):
#         if index % 2  == 0:
#             temp_list[index] = temp_list[index].upper()
#         else:
#             temp_list[index] = temp_list[index].lower()
#     return ''.join(temp_list)
#
# print(myfunc('afdSDFasdfsdfa'))
#
#
# # lambda expression, map, filter function
# def test_map(num):
#     return num**2
#
# my_nums = [1,2,3,4,5]
#
# for item in map(test_map, my_nums):
#     print(item)
#
# result = list(map(test_map, my_nums))
# print(result)
#
# def test_filter(num):
#     return num%2 ==0
#
# result2=list(filter(test_filter, my_nums))
# print(result2)
#
# lambda
# my_nums = [1,2,3,4,5]
# result=list(map(lambda num: num**2, my_nums))
# print(result)
# result2 = list(filter(lambda num: num%2 ==0, my_nums))
# print(result2)
