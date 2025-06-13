import unittest
import numpy as np

from pyconvex.supportFunction import *

class TestSupportFunction(unittest.TestCase):
    def testSupportFunction(self):
        self.assertEqual(supportFunction(np.array([-4]), 
                                         np.array([[1], [8]])), -4)
        self.assertEqual(supportFunction(np.array([1, -3]), 
                                         np.array([[0, 0], [2, 0], [0, 1]])), 2)
        self.assertEqual(supportFunction(np.array([5, 2]), 
                                         np.array([[3, 0], [0, 1], 
                                                   [2, 5], [5, 6], 
                                                   [7, 4], [6, 1]])), 43)
        self.assertEqual(supportFunction(np.array([3, -2, 5]), 
                                         np.array([[1, 0, 2], [5, 7, 6], 
                                                   [8, 2, 5], [6, 7, 1], 
                                                   [-5, 3, 0]])), 45)
        with self.assertRaises(ValueError):
            supportFunction(np.array([]), np.array([[1], [8]]))
        with self.assertRaises(ValueError):
            supportFunction(np.array([4]), np.array([]))


    def testSupportFunctionList(self):
        self.assertTrue(np.array_equal(
            supportFunctionList(np.array([[1, -3], [1, 2], [1, 3], [0, 6], 
                                          [-5, 2], [-3, -5], [0, -4], [1, -1]]), 
                                          np.array([[0, 0], [2, 0], [0, 1]])), 
                                          [2, 2, 3, 6, 2, 0, 0, 2]))
        with self.assertRaises(ValueError):
            supportFunctionList(np.array([[]]), np.array([[1,4], [8,1], [3,2]]))
        with self.assertRaises(ValueError):
            supportFunctionList(np.array([[4, 2], [5, 1], [2, -2]]), np.array([]))


if __name__ == '__main__':
    unittest.main()
