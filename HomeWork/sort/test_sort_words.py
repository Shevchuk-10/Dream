import unittest
from HomeWork.sort.sort_words import sort_words


class TestSort(unittest.TestCase):

    def test_empty_text(self):
        text = ''
        expected_result = ''
        result = sort_words(text)
        self.assertEqual(result, expected_result)

    def test_sort_words(self):
        text = 'Again some text for example. Hi , my name is Lux'
        expected_result = 'again example for hi is lux my name some text'
        result = sort_words(text)
        self.assertEqual(result, expected_result)

    def test_text_with_punctuation(self):
        text = 'Hello, man! How are you?'
        expected_result = 'are hello how man you'
        result = sort_words(text)
        self.assertEqual(result, expected_result)

    def test_up_register(self):
        text = 'Banana apple Orange Grapes Pear'
        expected_result = 'apple banana grapes orange pear'
        result = sort_words(text)
        self.assertEqual(expected_result,result)

    def test_special_char(self):
        text = '100 2 3 45 apples cats, dogs! oranges'
        expected_result = 'apples cats dogs oranges'
        result = sort_words(text)
        self.assertEqual(expected_result,result)


if __name__ == '__main__':
    unittest.main()