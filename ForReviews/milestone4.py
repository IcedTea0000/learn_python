# from collections import Counter
#
# mylist = "aaaaaaaaaaaaaaaabbbbbbbbbbcccccccccccccccddefghjasd"
# result = Counter(mylist)
# print(result)
# print(result.most_common(2))
# ==============================================================================================

# from collections import defaultdict
# d = defaultdict(lambda: "NA")
# d["k1"]: "v1"
# d["Not a key yet"]
# print(d["Not a key yet"])

# ==============================================================================================
# from collections import namedtuple
# Dog = namedtuple("Dog", ["age", "breed", "name"])
# sammy=Dog(breed="Husky", age=5, name="Sam")
# print(type(sammy))
# print(sammy.breed, sammy.age, sammy.name)

# ==============================================================================================
# import os
# os.getcwd()
# print(os.listdir())
#
# top_folder= "C:/Remy Martin/workspace/learn-python/"
# for folder, sub_folders, files in os.walk(top_folder):
#     print("Current: {}".format(folder))
#     print("Sub folders are: {}".format(sub_folders))
#     print("Files: {}".format(files))
#     print()

# ==============================================================================================
# import datetime
# my_time = datetime.time(1,2,3,4)
# print(my_time)
#
# print(datetime.date.today())

# ==============================================================================================
# import random
#
# print(random.randint(0, 111))
# random.seed(42)
# print(random.randint(0, 111))
# print(random.randint(0, 111))
# print(random.randint(0, 111))
# print(random.randint(0, 111))
#
# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 3, 4, 5, 6, 2, 4, 5, 6, 7]
# print(random.choice(mylist))
# print(random.choices(population=mylist, k=10))
#
# print(random.uniform(a=0,b=100))

# ==============================================================================================
# import pdb
# x=[1,2,3]
# y=2
# z=3
#
# result1= y+z
# pdb.set_trace()
# result2 = y+x

# ==============================================================================================
# def func_one(n):
#     return [str(num) for num in range(n)]
#
# def func_two(n):
#     return list(map(str, range(n)))
#
# import time
# star_time = time.time()
# func_one(1000000)
# end_time = time.time()
# elapsed_time1 = end_time- star_time
# print("elapsed time func1: {}".format(elapsed_time1))
#
# star_time = time.time()
# func_two(1000000)
# end_time = time.time()
# elapsed_time2 = end_time- star_time
# print("elapsed time func1: {}".format(elapsed_time2))


# import timeit
# stmt1 = """
# func_one(100)
# """
# setup1 = """
# def func_one(n):
#     return [str(num) for num in range(n)]
# """
# print(timeit.timeit(stmt=stmt1, setup=setup1, number = 1000))
#
# stmt2 = """
# func_two(100)
# """
# setup2 = """
# def func_two(n):
#     return list(map(str, range(n)))
# """
# print(timeit.timeit(stmt=stmt2, setup=setup2, number = 1000))
