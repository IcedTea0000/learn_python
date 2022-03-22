# class SampleClass():
#     pass
#
#
# my_class = SampleClass()
# print(my_class)

# ==============================================================================================
# class Dog():
#     species = "dog"
#
#     def __init__(self, mybreed, spots, name):
#         self.breed = mybreed
#         self.spots = spots
#         self.name = name
#
#     def __str__(self):
#         return "name: {}, breed: {}, spots: {}".format(self.name, self.breed, self.spots)
#
#
#     def bark(self, number):
#         print("WOOF! My name is {}, the number is {}".format(self.name, number))
#
#
# my_dog1 = Dog(mybreed="Lab", spots=False, name="Whisky")
# my_dog2 = Dog(spots=False, name="Whisky", mybreed="Lab")
#
# print(my_dog1.species)
# print(my_dog2)
#
# my_dog2.bark(4)

# ==============================================================================================
# class Animal():
#     def __init__(self):
#         print("animal created")
#
#     def eat(self):
#         print("animal is eating")
#
#     def speak(self):
#         raise NotImplementedError("Subclass must implement this abstract method")
#
#
# class Dog(Animal):
#     def __init__(self):
#         print("dog created")
#
#     def eat(self):
#         print("dog is eating")
#
#
# my_animal = Animal()
# my_animal.eat()
# my_dog = Dog()
# my_dog.eat()
#
#
# class Cat(Animal):
#     def __init__(self):
#         print("cat created")
#
#     def eat(self):
#         print("cat is eating")
#
#
# my_cat = Cat()
# for pet in [my_dog, my_cat]:
#     pet.eat()
# my_cat.speak()
# ==============================================================================================
# class Line:
#     def __init__(self, coor1, coor2):
#         self.coordinate1 = coor1
#         self.coordinate2 = coor2
#
#     def distance(self):
#         x1, y1 = self.coordinate1
#         x2, y2 = self.coordinate2
#         import math
#         result = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
#         return result
#
#     def slope(self):
#         x1, y1 = self.coordinate1
#         x2, y2 = self.coordinate2
#         result = (y2 - y1) / (x2 - x1)
#         return result
#
#
# coordinate1 = (1, 2)
# coordinate2 = (5, 8)
# line1 = Line(coordinate1, coordinate2)
# print(line1.distance())
# print(line1.slope())

# ==============================================================================================
# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#
#     def __str__(self):
#         return "Owner: {}, Balance: {}".format(self.owner, self.balance)
#
#     def deposit(self, amount):
#         self.balance = self.balance + amount
#         print("Deposit {} successful. Current balance: {}".format(amount, self.balance))
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Error withdraw. Available balance: {}".format(self.balance))
#         else:
#             self.balance = self.balance - amount
#             print("Withdraw {} successful. Current balance: {}".format(amount, self.balance))
#
#
# acc1 = Account(owner="Tim", balance=0)
# print(acc1)
# acc1.deposit(500)
# acc1.withdraw(600)
# acc1.withdraw(200)
# print(acc1)

# ==============================================================================================try except else finally
# result = None
# print("inside try, before error statement")
# result = 10/0
# print("inside try, after error statement")
#
# try:
#     print("inside try, before error statement")
#     # result = 10 / 1
#     result = 10/0
#     print("inside try, after error statement")
# except ValueError:
#     print("inside except")
#     print("valueError occurs")
# except ZeroDivisionError:
#     print("inside except")
#     print("ZeroDivisionError occurs")
# except:
#     print("inside except")
#     print("all other exceptions")
# finally:
#     print("inside finally")

# result = None
# for divider in range (-10, 5):
#     try:
#         result = 10/divider
#         print("{} / {} = {}".format(10, divider, result))
#     except:
#         print("error divider: {}".format(divider))
#         continue
#     else:
#         print("correct divider")
#         break

# try:
#     with open("not_exist.txt") as file:
#         print(file)
#     # print("try block")
# except FileNotFoundError as error:
#     print(f"exception {error} happen")
# else:
#     print("else after try block")
# finally:
#     file.close()
#     print("finally block")
# ==============================================================================================raise your own exception
# height = float(input("input height: "))
# if height > 3:
#     raise ValueError("Human height should not be over 3 meters")

# ==============================================================================================
"""
doc-string test for pylint
"""
# from math import sqrt
#
#
# def ask():
#     num = None
#     while True:
#         try:
#             num = int(input("Enter number : "))
#         except ValueError:
#             print("Only number allowed.")
#         else:
#             break
#     print("Square: {}".format(sqrt(num)))
#
#
# ask()
