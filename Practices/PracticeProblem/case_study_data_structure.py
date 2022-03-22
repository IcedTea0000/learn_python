import string
import json
import re


def get_all_words(file_path):
    """

    :param file_path: file .txt path
    :return: set of lowercase words in text file
    """

    """
    1. read each line of text file
    2. convert line to set of words, strip all white space and punctuation
    3. append set to result set
    """
    result_set = set()
    with open(file_path) as text_file:
        for line in text_file:
            word_list = line.split(' ')
            for word in word_list:
                result_set.add(word.strip(string.punctuation).lower())
    return result_set


def export_book_data(file_path):
    """
    count the total number of words in the book, and the
    number of times each word is used
    :param file_path: input .txt of book file
    :return: return dictionary of data about the .txt
    """
    result_dict = {'word_count': '', 'word_frequencies': {}}
    word_frequenies_dict = {}
    total_word_count = 0
    list_word_cleaned = []
    with open(file_path) as text_file:
        list_word = text_file.read().replace('\n', ' ').split(' ')
        for word in list_word:
            list_word_cleaned.append(word.strip(string.punctuation))
    total_word_count = len(list_word_cleaned)

    for word in list_word_cleaned:
        word_frequenies_dict[word] = word_frequenies_dict.get(word, 0) + 1

    result_dict['word_count'] = total_word_count
    result_dict['word_frequencies'] = word_frequenies_dict
    return result_dict


if __name__ == '__main__':
    file_path = '/ObjectAndDataStructure\\crime_book.txt'
    # get_all_words(file_path)
    print(json.dumps(export_book_data(file_path), indent=2))
