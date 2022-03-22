import unittest


def cap_text(text):
    return text.title()


class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = 'martin hoang'
        result = cap_text(text)
        self.assertEqual(result, 'Martin Hoang')


if __name__ == '__main__':
    unittest.main()
