import unittest
from HomeWork.vowels import vowels

class TestVowels(unittest.TestCase):
    '''Проверка,возвращает ли фунция count_vowels правильный результат'''
    def test_count_vowels(self):
        self.assertEqual(vowels.count_vowels('aeiouAEIOU'), 10)

if __name__ == '__main__':
    unittest.main()
