import unittest

from PIL import Image

import image_comparer


class MyTestCase(unittest.TestCase):
    def test_comparer(self):
        result = 23.696326053231388

        original = Image.open("imgs/original.png")
        edited = Image.open("imgs/edited.png")

        self.assertEqual(result, image_comparer.rmsdiff(original, edited))


if __name__ == '__main__':
    unittest.main()
