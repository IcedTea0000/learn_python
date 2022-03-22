"""input data:
four score and seven years ago

answer:
oga sraey neves dna erocs ruof"""


def reverse_string1(input_string):
    return input_string[::-1]


def reverse_string2(input_string):
    temp_list = []
    for character in input_string:
        temp_list.append(character)
    temp_list.reverse()
    return ''.join(temp_list)


def reverse_string3(input_string):
    temp_list = list(input_string)
    temp_list.reverse()
    return ''.join(temp_list)


if __name__ == '__main__':
    text = 'four score and seven years ago'
    print(reverse_string1(text))
    print(reverse_string2(text))
    print(reverse_string3(text))
