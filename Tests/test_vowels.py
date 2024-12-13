import unittest
from HomeWork.vowels.vowels import count_vowels  # Імпорт функції, якщо вона знаходиться в іншому файлі


class TestCountVowels(unittest.TestCase):

    def test_text_with_vowels(self):
        text = 'HELLO'
        expected_result = 2  # Голосні: E, O
        result = count_vowels(text)
        self.assertEqual(result, expected_result)

    def test_text_with_numbers_and_punctuation(self):
        text = 'Th3 qu!ck brOwn f0x.'
        expected_result = 2  # Голосні: o, o (ігноруємо числа і символи)
        result = count_vowels(text)
        self.assertEqual(result, expected_result)

    def test_text_with_mixed_case(self):
        text = 'AaaEeiIoOuU'
        expected_result = 11  # Голосні: A, a, a, E, e, i, I, o, O, u, U
        result = count_vowels(text)
        self.assertEqual(result, expected_result)

    def test_empty_text(self):
        text = ''
        expected_result = 0  # Порожній рядок не містить голосних
        result = count_vowels(text)
        self.assertEqual(result, expected_result)

    def test_text_with_no_vowels(self):
        text = 'bcdfghjklmnpqrstvwxyz'
        expected_result = 0  # Немає голосних
        result = count_vowels(text)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
