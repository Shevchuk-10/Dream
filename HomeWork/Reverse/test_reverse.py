import unittest


class TestReverse(unittest.TestCase):
    def test_reverse(self):
        text = ['Today', 'is', 'a', 'very', 'good', 'day', 'and', 'sun']

        # Ожидаемый результат после переворота списка
        expected_result = ['sun', 'and', 'day', 'good', 'very', 'a', 'is', 'Today']
        text.reverse()
        self.assertEqual(text, expected_result)


if __name__ == '__main__':
    unittest.main()
