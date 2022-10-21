import encode_morse as em
import unittest

class TestMorseCode(unittest.TestCase):

    def test_morsecode(self):
        self.assertEqual(em.encode_morse("hello there"), ".... . .-.. .-.. ---   - .... . .-. .")
        self.assertEqual(em.encode_morse("EDABBIT CHALLENGE"), '. -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. .')
        self.assertEqual(em.encode_morse("HELP ME !"), ".... . .-.. .--.   -- .   -.-.--")

if __name__ == '__main__':
    unittest.main()