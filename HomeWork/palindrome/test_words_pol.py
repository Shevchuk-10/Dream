import unittest
from HomeWork.palindrome.words_pol import palindromes

class TestPal(unittest.TestCase):
    def test_palindrome(self):
        text = "I'm level, I'm radar!"
        expected_result = ['i', 'm', 'level', 'i', 'm', 'radar']
        palindromes_result = palindromes(text)
        self.assertEqual(palindromes_result, expected_result)

    def test_empty_palindrome(self):
        text = ''
        expected_result = []
        palindromes_result = palindromes(text)
        self.assertEqual(palindromes_result, expected_result)

    def test_none_palindrome(self):
        text = 'Пример Слов'
        expected_result = []  # Тут не є паліндромом, тому результат буде порожнім списком
        palindromes_result = palindromes(text)
        self.assertEqual(palindromes_result, expected_result)

    def test_case_insensitivity(self):
        text = 'Madam in Eden I’m Adam'
        expected_result = ['madam', 'i', 'm',]
        palindromes_result = palindromes(text)
        self.assertEqual(palindromes_result, expected_result)

    def test_single_characters(self):
        text = 'a b c d '
        expected_result = ['a','b','c','d']
        palindromes_result = palindromes(text)
        self.assertEqual(palindromes_result,expected_result)

    def test_with_spaces(self):
        text = '  madam  i  m  '
        expected_result = ['madam', 'i', 'm']
        palindromes_result = palindromes(text)
        self.assertEqual(palindromes_result, expected_result)

    def test_numbers(self):
        text = '12321 45654 789'
        expected_result = ['12321', '45654']
        palindromes_result = palindromes(text)
        self.assertEqual(palindromes_result,expected_result)


if __name__ == '__main__':
    unittest.main()



