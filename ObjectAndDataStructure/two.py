# two.py
from ObjectAndDataStructure import one


def func():
    print('func() in two.py')


print('TOP LEVEL IN TWO.PY')
one.func()

if __name__ == '__main__':
    print('TWO.PY is being rung directly')
else:
    print('TWO.PY is imported')
