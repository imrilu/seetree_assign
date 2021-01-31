import unittest
from data_handler import *


class DataTest(unittest.TestCase):
    """
    Simple test for data handler only
    """

    def test_init(self):
        print("start data handler test init")
        self.assertIsInstance(images, dict)
        self.assertIsInstance(polygons, dict)
        self.assertFalse(check_can_calculate_relations())
        load_images()
        self.assertTrue(images)
        self.assertFalse(check_can_calculate_relations())
        load_polygons()
        self.assertTrue(polygons)
        self.assertTrue(check_can_calculate_relations())


if __name__ == '__main__':
    unittest.main()
