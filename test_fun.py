import fun

import unittest

class myTest(unittest.TestCase):

    def test_add(self):
        result = fun.add(1,2)
        self.assertEqual(result,4)


if __name__ == '__main__':
    unittest.main()