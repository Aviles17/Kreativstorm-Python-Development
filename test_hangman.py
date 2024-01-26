import unittest
from hangman import hangman_game, check_letter

class TestHangman(unittest.TestCase):

    def test_check_letter(self):
        self.assertEqual(check_letter('a', 'apple', '_____'), 'a____')
        self.assertEqual(check_letter('p', 'apple', 'a____'), 'app__')
        self.assertEqual(check_letter('z', 'apple', 'app__'), 'app__')

if __name__ == '__main__':
    unittest.main()