import unittest
from soundex import get_soundex


class TestSoundex(unittest.TestCase):

    def test_get_soundex(self):
        test_data = {
            'Lietuva': 'L310',
            'summer': 'S560',
            'Ukraine': 'U265',
            'Bayraktar': 'B623',
            'logic': 'L220',
            'correct': 'C623',
            'Ashcraft': 'A261',
            'Pfister': 'P236',
            'Tymczak': 'T522',
            'Rupert': 'R163',
            'Rubin': 'R150',
            'Ashcroft': 'A261'}
        for text in test_data:
            result = get_soundex(text)
            expected = test_data[text]
            self.assertEqual(
                expected,
                result
            )
