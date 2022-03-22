import sys


def rotation(text, number_to_rotate):
    """Cypher encrypt, add a character to a number"""
    converted_list = []
    output_text = ''
    for character in text:
        converted_list.append(ord(character) - number_to_rotate)
    for number in converted_list:
        output_text += chr(number)
    return output_text


def check_word_longer_than(path, word_length):
    """read file text.txt line by line, print words that longer than word_length"""
    with open(path, mode='r') as text_file:
        for line in text_file:
            text = line.strip()
            if len(text) > word_length:
                print('text : {} | size : {} bytes'.format(text, sys.getsizeof(line)))


def has_no_e(word):
    return 'e' in word.lower()


def check_word_no_e(path):
    """print only the words that have no
    'e' and compute the percentage of the words in the list that have no 'e'"""
    total_word_count = 0
    total_word_has_e = 0
    with open(path, mode='r') as text_file:
        for line in text_file:
            text = line.strip()
            if not has_no_e(text):
                print(text)
                total_word_has_e += 1
            total_word_count += 1
    print('Total word has e : {} / {}'.format(total_word_has_e, total_word_count))
    print('Percent word has e : {} %'.format(total_word_has_e / total_word_count * 100))


def has_no_forbidden(word, forbidden_letters):
    for letter in forbidden_letters:
        if letter in word:
            return False
    return True


def check_word_no_forbidden(path, forbidden_letters):
    """user to enter a string of forbidden letters and
    then print the number of words that don’t contain any of them"""
    total_word_count = 0
    total_word_not_has_forbidden = 0
    with open(path, mode='r') as text_file:
        for line in text_file:
            text = line.strip()
            if has_no_forbidden(text, forbidden_letters):
                print(text)
                total_word_not_has_forbidden += 1
            total_word_count += 1
    print('Total words not has forbidden : {} / {}'.format(total_word_not_has_forbidden, total_word_count))
    print('Percent word not has forbiden : {} %'.format(total_word_not_has_forbidden / total_word_count * 100))


def check_open_file(path, forbidden_letters):
    """check file text, print line that not contain any forbidden letter"""
    text_file = open(path, mode='r')
    total_word_count = 0
    total_word_not_has_forbidden = 0
    for line in text_file:
        text = line.strip()
        if has_no_forbidden(text, forbidden_letters):
            print(text)
            total_word_not_has_forbidden += 1
        total_word_count += 1
    print('Total words not has forbidden : {} / {}'.format(total_word_not_has_forbidden, total_word_count))
    print('Percent word not has forbiden : {} %'.format(total_word_not_has_forbidden / total_word_count * 100))


def print_palindrome(number_of_digit):
    """print all palindrome string from 0 to cap"""
    result_count = 0
    cap_number = 10 ** number_of_digit
    for index in range(0, cap_number):
        number_to_text = str(index)
        number_to_text = '0' * (number_of_digit - len(number_to_text)) + number_to_text  # convert to format 000xxx
        if number_to_text == number_to_text[::-1]:
            result_count += 1
            print(number_to_text)
    print('Result count : {}'.format(result_count))


if __name__ == '__main__':
    # print(rotation('abc', 1))
    path = 'C:\\workspace\\learn-python\\Practices\\text.txt'
    path2 = 'C:\\workspace\\learn-python\\Practices\\1million word list.txt'
    # check_word_longer_than(path, 20)
    # check_word_no_e(path)
    # check_word_no_forbidden(path2, 'abc')
    # check_open_file(path2, 'abc')

    print_palindrome(number_of_digit=6)
