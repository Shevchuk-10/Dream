import unittest
from HomeWork.numbers.num_in_str import numbers_in_string


class TestNum(unittest.TestCase):
    def test_numbers_in_string(self):
        text = 'Есть например 56 Айфонов и 6 флешок.'
        expected_result = 62
        num_result = numbers_in_string(text)
        self.assertEqual(expected_result, num_result)

    def test_no_numbers(self):
        text = 'Это текст без чисел'
        result = numbers_in_string(text)
        self.assertEqual(result, 0)

    def test_empty_str(self):
        text = ''
        expected_result = 0
        result = numbers_in_string(text)
        self.assertEqual(expected_result, result)

    def test_numbers_with_text(self):
        text = 'Текст 100 и 50 числа'
        result = numbers_in_string(text)
        self.assertEqual(result, 150)

    def test_multiple_numbers(self):
        text = '1 2 3 4 5'
        result = numbers_in_string(text)
        self.assertEqual(result, 15)

    def test_special_char(self):
        text = 'Число 12* и 50?:% Это тест с символами +)_(*?:%%;№"!'
        result = numbers_in_string(text)
        self.assertEqual(result, 62)  # Ожидаем 12 + 50 = 62


if __name__ == '__main__':
    unittest.main()
