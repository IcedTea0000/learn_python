def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x ** 3)
    return result


def create_cubes2(n):
    for x in range(n):
        yield x ** 3


# print(create_cubes(10))
#
# for value in create_cubes(10):
#     print(value)

# for value in create_cubes2(10):
#     print(value)


def iterator_example(text=''):
    text_iter = iter(text)
    print(next(text_iter))


# iterator_example('test')

def test_iter():
    list1=[1,2]
    list1_iter = iter(list1)
    print(next(list1_iter))
    list1.append(3)
    print(next(list1_iter))
    print(next(list1_iter))

test_iter()