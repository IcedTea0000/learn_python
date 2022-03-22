def make_histogram(s):
    """

    :param s: text
    :return: dictionary of histogram {letter : appearance}
    """
    historgram = {}
    for letter in s:
        historgram[letter] = historgram.get(letter, 0) + 1
    return historgram


def most_frequent(text):
    """

    :param text: input text
    :return: list of letter in reverse order of frequency
    """
    histogram = make_histogram(text)
    reversed_histogram_list = []
    for letter, frequency in histogram.items():
        reversed_histogram_list.append((frequency, letter))

    reversed_histogram_list.sort(reverse=True)
    result = []

    for frequency, letter in reversed_histogram_list:
        result.append(letter)
    return result

def is_anagram(text1, text2):
    """

    :param text1: input text
    :param text2: input text
    :return: true if 2 texts are anagram, false if 2 texts are not
    """
    list_text1 = sorted(text1)
    list_text2 = sorted(text2)
    return list_text1 == list_text2

def get_lists_of_anagram(file_path):
    """

    :param file_path: file .txt input
    :return: tuple of lists of anagram
    """
    pass


if __name__ == '__main__':
    # print(most_frequent('aaaabbc'))
    pass
