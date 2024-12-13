import unittest
from HomeWork.big_small.big_small import big_small


class TestBigSmall(unittest.TestCase):

    def test_empty_text(self):
        # Тест для порожнього тексту
        text = ''
        expected_result = 'Текст пустой'

        # Захоплюємо виведення через logging
        with self.assertLogs('root', level='INFO') as log:
            big_small(text)
            self.assertIn(expected_result, log.output[0])

    def test_single_word(self):
        # Тест для одного слова
        text = 'Python'
        expected_long = 'Python'
        expected_short = 'Python'

        # Захоплюємо виведення через logging
        with self.assertLogs('root', level='INFO') as log:
            big_small(text)

        # Перевірка, чи є правильний результат
        self.assertIn(f'Самое длинное слово: {expected_long}', log.output[0])
        self.assertIn(f'Самое короткое слово: {expected_short}', log.output[1])

    def test_multiple_words(self):
        # Тест для декількох слів
        text = 'This is a simple test case'
        expected_long = 'simple'
        expected_short = 'a'

        # Захоплюємо виведення через logging
        with self.assertLogs('root', level='INFO') as log:
            big_small(text)

        # Перевірка, чи є правильний результат
        self.assertIn(f'Самое длинное слово: {expected_long}', log.output[0])
        self.assertIn(f'Самое короткое слово: {expected_short}', log.output[1])

    def test_words_with_special_characters(self):
        # Тест для слів із спеціальними символами
        text = 'Hello world! Python@'
        expected_long = 'Python@'
        expected_short = 'Hello'

        # Захоплюємо виведення через logging
        with self.assertLogs('root', level='INFO') as log:
            big_small(text)

        # Перевірка, чи є правильний результат
        self.assertIn(f'Самое длинное слово: {expected_long}', log.output[0])
        self.assertIn(f'Самое короткое слово: {expected_short}', log.output[1])

    def test_same_length_words(self):
        # Тест для слів однакової довжини
        text = 'cat dog bat'
        expected_long = 'cat'  # будь-яке з цих слів
        expected_short = 'cat'  # будь-яке з цих слів

        # Захоплюємо виведення через logging
        with self.assertLogs('root', level='INFO') as log:
            big_small(text)

        # Перевірка, чи є правильний результат
        self.assertIn(f'Самое длинное слово: {expected_long}', log.output[0])
        self.assertIn(f'Самое короткое слово: {expected_short}', log.output[1])


if __name__ == '__main__':
    unittest.main()