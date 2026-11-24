
import unittest
import numpy as np


class TestSignal(unittest.TestCase):

    def test_first_value(self):
        t = 0
        s = np.cos(10 * t) + np.cos(11 * t)
        self.assertEqual(s, 2)

    def test_envelope(self):
        t = 0
        a = 2 * np.cos((10 - 11) * t / 2)
        self.assertEqual(a, 2)

    def test_points(self):
        t = np.linspace(0, 20, 1000)
        self.assertEqual(len(t), 1000)

    def test_max_value(self):
        t = np.linspace(0, 20, 1000)
        s = np.cos(10 * t) + np.cos(11 * t)
        self.assertTrue(np.all(np.abs(s) <= 2))


if __name__ == '__main__':
    unittest.main()
