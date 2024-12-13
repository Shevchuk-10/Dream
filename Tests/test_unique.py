import unittest
from HomeWork.unique.unique_words import word

class TestUnique(unittest.TestCase):
    def test_word(self):
        input_text = 'My mom is a by Iphone and i a by MacBook'
        expected_result = 9  # Очікувана кількість унікальних слів
        self.assertEqual(word(input_text), expected_result)

    def test_no_word(self):
        text = ''
        expected_result = 0
        result = word(text)
        self.assertEqual(expected_result,result)

if __name__ == '__main__':
    unittest.main()
