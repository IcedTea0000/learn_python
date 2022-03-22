def my_function1():
    print("one.py my_function1")


print("one.py outside '__main__' print statement")

if __name__ == "__main__":
    print("one.py inner '__main__' print statement")
    print("one.py is being run directly")
else:
    print("one.py is being imported")
