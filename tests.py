import unittest

from main import Analizer


class AnalizerTest(unittest.TestCase):

    def test_normilize_text(self):
        result = Analizer._Analizer__normalize_text("Hello, world. It's me - Python! To do: find some features...")
        self.assertEqual(result, "hello world. it's me python! to do find some features...")
