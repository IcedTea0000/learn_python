t = (1, 'string', 3)


# print(t.count(1))

# a = 1, 2
# b= 3, 4
# c, d = a
# print(c,d)

def test_gather_args(*args):
    print(args)


test_gather_args(1, 2, 3, 4)

# zip() only combine the euqal amount of member between 2 interabe
s = 'abc'
t = [1, 2]
z = 'xyz'
for pair in zip(s, z):
    print(pair)


directory = dict()
first = 'John'
last = 'Wick'
directory[first, last] = '0991238483'
print(directory)
