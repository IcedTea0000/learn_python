# one.py

def func():
    print('func() in one.py')


print('TOP LEVEL IN ONE.PY')

if __name__ == '__main__':
    print('ONE.PY is being rung directly')
else:
    print('ONE.PY is imported')
