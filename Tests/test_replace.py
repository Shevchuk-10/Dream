import unittest
from HomeWork.replace.replace import replace_wo


class TestRep(unittest.TestCase):

    def test_avarage(self):
        # Тест для порожнього тексту
        text = ''
        expected_result = ''  # Порожній рядок
        result = replace_wo(text)
        self.assertEqual(result, expected_result)

    def test_s_or_S(self):
        # Тест для слів на "s" або "S"
        text = 'She sells a new snap and sneakers'
        expected_result = 'Python Python a new Python and Python'
        result = replace_wo(text)
        self.assertEqual(result, expected_result)

    def test_none_s_or_S(self):
        # Тест, коли немає слів на "s" або "S"
        text = 'Hello World'
        expected_result = 'Hello World'
        result = replace_wo(text)
        self.assertEqual(result, expected_result)

    def test_only_sS(self):
        # Тест, коли всі слова починаються на "s" або "S"
        text = 'She sell sneakers'
        expected_result = 'Python Python Python'
        result = replace_wo(text)
        self.assertEqual(result, expected_result)

    def test_one_word(self):
        # Тест для одного слова
        text = 'sun'
        expected_result = 'Python'
        result = replace_wo(text)
        self.assertEqual(result, expected_result)

    def test_up_register(self):
        # Тест для великої літери
        text = 'She Sell Sneakers'
        expected_result = 'Python Python Python'
        result = replace_wo(text)
        self.assertEqual(result, expected_result)

    def test_special_characters(self):
        # Тест з спеціальними символами
        text = 'She@ sells* sneakers+!'
        expected_result = 'Python Python Python'
        result = replace_wo(text)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
