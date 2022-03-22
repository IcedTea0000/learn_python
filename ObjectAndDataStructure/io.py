import sys

test_file = 'C:\\Remy Martin\\workspace\\learn-python\\ObjectAndDataStructure\\test_file.txt'

# test_file = open('C:\\Remy Martin\\workspace\\learn-python\\ObjectAndDataStructure\\test_file.txt')
# print(test_file.read())
# print(test_file.seek(0))
# print(test_file.read())
# print(sys.getsizeof(test_file))

# print(test_file.readlines())

# print(test_file.readline())
# print(test_file.readline())

# with open('C:\workspace\learnPython\ObjectAndDataStructure\/test_file.txt', mode='r') as new_file:
#     for line in new_file:
#         print('Content \n', line)
#         print('File size: ', sys.getsizeof(line))

with open(test_file, mode='r') as new_file:
      print(new_file.readline())

