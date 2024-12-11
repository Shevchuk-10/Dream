import unittest
from HomeWork.long.long_in_words import long_words


class TestLong(unittest.TestCase):

    def test_average_words(self):
        text = 'Пример текста'
        expected_result = 6.0
        result = long_words(text)
        self.assertEqual(result,expected_result)

    def test_average_single_word(self):
        text = 'Тест'
        expected_result = 4.0
        result = long_words(text)
        self.assertEqual(result,expected_result)

    def test_average_empty_word(self):
        text = ''
        expected_result = 0
        result = long_words(text)
        self.assertEqual(result,expected_result)

    def test_average_lond_word(self):
        text = 'ДлинноеСлово'
        expected_result = 12.0
        result = long_words(text)
        self.assertEqual(result,expected_result)


if __name__ == '__main__':
    unittest.main()












