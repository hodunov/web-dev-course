from django.test import TestCase

from core.templatetags.core_tags import count_words, get_even_numbers


class CustomTagTest(TestCase):

    def test_count_words(self):
        result = count_words("Dori me Interimo adapare, dori me Ameno, ameno, latire Latiremo, dori me")
        expected_result = 12
        self.assertEqual(result, expected_result, msg="Should be 12")

    def test_get_even_numbers(self):
        result = get_even_numbers([1, 2, 3, 4, 5, 6])
        expected_result = [2, 4, 6]
        self.assertEqual(result, expected_result, msg="Should be [2, 4, 6]")
