import json


def cumulative_sum(input_list=[]):
    """takes a list of numbers and returns the cumulative
    sum; that is, a new list where the ith element is the sum of the first i+1 elements from
    the original list.
    """
    cumulative_sum_list = []
    for index in range(0, len(input_list)):
        new_value = 0
        for sub_index in range(0, index + 1):
            new_value += input_list[sub_index]
        cumulative_sum_list.append(new_value)
    return cumulative_sum_list


def middle(input_list=[]):
    """takes a list and returns a new list that contains all
    but the first and last elements"""
    if len(input_list) == 1:
        input_list.pop(0)
    if len(input_list) > 1:
        input_list.pop(0)
        input_list.pop(-1)
    return input_list


def chop(input_list=[]):
    """takes a list, modifies it by removing the first and last
    elements, and returns None"""
    if len(input_list) == 1:
        input_list.pop(0)
    if len(input_list) > 1:
        input_list.pop(0)
        input_list.pop(-1)


def is_sorted(input_list=[]):
    """ takes a list as a parameter and returns True if
    the list is sorted in ascending order and False otherwise."""
    temp_list = sorted(input_list, reverse=False)
    return input_list == temp_list


def has_duplicates1(input_list=[]):
    """ takes a list and returns True if there is
    any element that appears more than once. It should not modify the original list"""
    temp_list = input_list.copy()
    while len(temp_list) != 0:
        var_to_compare = temp_list.pop(0)
        if var_to_compare in temp_list:
            return True
    return False


def has_duplicates2(input_list=[]):
    """ takes a list and returns True if there is
    any element that appears more than once. It should not modify the original list"""
    temp_set = set(input_list)
    return not len(temp_set) == len(input_list)


def count_char(input_list=[]):
    """
    input: list
    output: dictionary with key=character, value=count number of character
    """
    result_dict = {}
    for member in input_list:
        if member not in result_dict:
            result_dict.update({member: 1})
        else:
            result_dict[member] += 1
    return result_dict


if __name__ == '__main__':
    # print(cumulative_sum([]))
    # print(middle([1, 2, 3, 4, 5]))

    # test_list = [1, 2, 3, 4]
    # chop(test_list)
    # print(test_list)

    # print(is_sorted(test_list))

    # test_list = []
    # print(has_duplicates1(test_list))
    # print(has_duplicates2(test_list))

    test_list = [1, 1, 1, 2, 3, 3, 3, 3, 3, 4, 5, 6]
    print(json.dumps(count_char(test_list), indent=2))
