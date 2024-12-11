import unittest
from HomeWork.unique.unique_words import word

class TestUnique(unittest.TestCase):
    def test_word(self):
        input_text = 'My mom is a by Iphone and i a by MacBook'
        expected_result = 9  # Очікувана кількість унікальних слів

        self.assertEqual(word(input_text), expected_result)

if __name__ == '__main__':
    unittest.main()
