# assign b = a =, then both variables refer to the same immutable object
# But when first variable is changed, 2 variables will now point to different objects
# however, with other types of object, 2 var still point to same object

# c = 1
# d = c
# print(d is c)  # true
# c -= 1
# print(d is c)  # false
#
# c = [1, 2, 3]
# d = c
# print(d is c) # true
# c.pop(1)
# print(d is c)  # true
#
# c = 'test'
# d = c
# print(d is c) # true

def increment(n):
    n += 1


def test_list(list):
    list.append(1)


if __name__ == '__main__':
    a = 0
    increment(a)
    print(a)

    list = [1, 2]
    test_list(list)
    print(list)
