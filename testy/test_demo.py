
from unittest import TestCase


class TestDemo(TestCase):

    def test_assertion_types(self):
        self.assertEqual(2, 1+1)
        self.assertNotEqual(5, 1+1)
        self.assertTrue( 10 > 1)
        self.assertFalse(10 < 1)
