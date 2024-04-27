import unittest
from unittest.mock import patch
from target_en import generate_grid, get_words, get_user_words, get_pure_user_words

class TestTargetEnStart(unittest.TestCase):
    def test_generate_grid(self):
        grid = generate_grid()
        self.assertEqual(len(grid), 3)
        self.assertEqual(len(grid[0]), 3)
        self.assertEqual(len(grid[1]), 3)
        self.assertEqual(len(grid[2]), 3)
        vowels = ['A', 'E', 'I', 'O', 'U']
        vowel_count = 0
        for row in grid:
            for letter in row:
                self.assertTrue(letter.isupper())
                if letter in vowels:
                    vowel_count += 1
        self.assertEqual(vowel_count, 3)

    def test_get_words(self):
        words = get_words('test_dict.txt', ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])
        self.assertEqual(words, ['abed', 'bead', 'cafe', 'fade'])

    @patch('builtins.input', side_effect=['test', 'words', EOFError])
    def test_get_user_words(self, mock_input):
        user_words = get_user_words()
        self.assertEqual(user_words, ['test', 'words']) 

    @patch('builtins.input', side_effect=[EOFError])
    def test_get_user_words_no_input(self, mock_input):
        user_words = get_user_words()
        self.assertEqual(user_words, [])

    def test_get_words_invalid_letters(self):
        words = get_words('test_dict.txt', ['1', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])
        self.assertEqual(words, [])

    def test_case_sensitivity(self):
        words = get_words('test_dict.txt', ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])
        self.assertEqual(words, ['abed', 'bead', 'cafe', 'fade'])

    @patch('builtins.input', side_effect=['TEST', 'WORDS', EOFError])
    def test_get_user_words_uppercase(self, mock_input):
        user_words = get_user_words()
        self.assertEqual(user_words, ['TEST', 'WORDS'])
    #found matches and errors
    def test_get_words_non_english_letters_a(self):
        words = get_words('test_dict.txt', ['å', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])
        self.assertEqual(words, [])

    def test_get_words_non_english_letters_b(self):
        words = get_words('test_dict.txt', ['q', 'w', 'r', 'y', 'o', 'f', 'g', 'h', 'i'])
        self.assertEqual(words, [])

    def test_get_words_non_english_letters_error(self):
        words = get_words('test_dict.txt', [])
        self.assertEqual(words, [])

    def test_get_words_empty_file(self):
        words = get_words('empty.txt', ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])
        self.assertEqual(words, [])

    def test_get_words_non_existent_file(self):
        with self.assertRaises(FileNotFoundError):
            get_words('non_existent.txt', ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])

    @patch('builtins.input', side_effect=['test', 'test', EOFError])
    def test_get_user_words_duplicate_words(self, mock_input):
        user_words = get_user_words()
        self.assertEqual(user_words, ['test', 'test'])

    @patch('builtins.input', side_effect=['test1', 'word!', EOFError])
    def test_get_user_words_non_letter_characters(self, mock_input):
        user_words = get_user_words()
        self.assertEqual(user_words, ['test1', 'word!'])

    def test_get_pure_user_words(self):
        user_words = ['test', 'words', 'stew', 'rode']
        letters = ['t', 'e', 's', 'w', 'o', 'r', 'd', 'a', 'b']
        words_from_dict = ['test', 'words']
        pure_user_words = get_pure_user_words(user_words, letters, words_from_dict)
        self.assertEqual(pure_user_words, ['rode'])

if __name__ == '__main__':
    unittest.main()
