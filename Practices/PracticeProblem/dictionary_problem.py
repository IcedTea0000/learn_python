import json


def frequency_dict(input_list=[]):
    """

    :param input_list: any list
    :return: dictionary with K=list member, V = number of appear
    """
    result_dict = dict()
    for member in input_list:
        if member not in result_dict:
            result_dict.update({member: 1})
        else:
            result_dict[member] += 1
    return result_dict


def inverse_frequency_dict1(input_dict={}):
    """

    :param input_dict: frequency dictionary
    :return: dictionary with K=number of appearance, V = list of member
    """
    total_loop_count = 0
    result_dict = dict()
    appearance_set = set(input_dict.values())
    for appearance in appearance_set:
        result_dict.update({appearance: []})
        for member in input_dict:
            total_loop_count += 1
            if input_dict[member] == appearance:
                result_dict[appearance].append(member)
    print('Total loop count {}'.format(total_loop_count))
    return result_dict


def inverse_frequency_dict2(input_dict={}):
    """

    :param input_dict: frequency dictionary
    :return: dictionary with K=number of appearance, V = list of member
    """
    total_loop_count = 0
    result_dict = dict()
    for character in input_dict:
        total_loop_count += 1
        char_count = input_dict[character]
        if char_count not in result_dict:
            result_dict[char_count] = [character]
        else:
            result_dict[char_count].append(character)
    print('Total loop count {}'.format(total_loop_count))
    return result_dict


def inverse_frequency_dict3(input_dict={}):
    """

    :param input_dict: frequency dictionary
    :return: dictionary with K=number of appearance, V = list of member
    """
    total_loop_count = 0
    result_dict = dict()
    for character in input_dict:
        total_loop_count += 1
        char_count = input_dict[character]
        result_dict.setdefault(char_count, []).append(
            character)  # check if key char_count not exist, if not create an empty list for value, then append character
    print('Total loop count {}'.format(total_loop_count))
    return result_dict


if __name__ == '__main__':
    test_list = ['a', 'a', 'b', 'b', 'c', 'c', 'c']
    print(json.dumps(inverse_frequency_dict1(frequency_dict(test_list)), indent=2))
    print(json.dumps(inverse_frequency_dict2(frequency_dict(test_list)), indent=2))
    print(json.dumps(inverse_frequency_dict3(frequency_dict(test_list)), indent=2))

    pass
