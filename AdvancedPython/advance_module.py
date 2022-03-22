# counter module
from collections import Counter


def counter_test(input):
    return Counter(input)


print(counter_test([1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3]))
print(counter_test('asaaasdfasdfasv'))
print(
    counter_test('this is a sentence for a testing purpose that i am not sure what i am writing about'.lower().split()))

print(Counter('asfdassdvbxczvzvasfafadf').most_common(5))

# defaultdict module
from collections import defaultdict

d = {'a': 1}
d = defaultdict(lambda: 0)
print(d['wrong_key'])
print(d['a'])

# namedtuple module
from collections import namedtuple

Customer = namedtuple('Customer', ['name', 'age', 'address'])
martin = Customer(name='Martin', age=27, address='Here')
print(type(martin))
print(martin)
