import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../HomeWork')))

from HomeWork.letter.one_letter import letter

class TestLetterFunction(unittest.TestCase):
    def test_letter(self):
        self.assertEqual(letter('Level apple radar chery civic'), ['level', 'radar', 'civic'])
        self.assertEqual(letter('apple banana cherry'), [])
        self.assertEqual(letter(''), [])
        self.assertEqual(letter('a b c d e'), ['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(letter('Level LEVEL level'), ['level', 'level', 'level'])
        self.assertEqual(letter('deified rotator pop'), ['deified', 'rotator', 'pop'])

if __name__ == '__main__':
    unittest.main()
