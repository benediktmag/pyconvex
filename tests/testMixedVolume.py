import unittest

from pyconvex.mixedVolume import *

class TestSupportFunction(unittest.TestCase):
    def testMixedVolume(self):
        self.assertEqual(mixedVolume([[[0,0], [1,0], [0,2], [1,2]], 
                                     [[0,0], [3,0], [0,4], [3,4]]]), 5.0)
        self.assertEqual(mixedVolume([[[1,5], [3,9], [4,2]], 
                                     [[2,4], [2,6]]]), 3.0)

        # Testing that the mixed volume of the same body is equal to the volume 
        # of that body
        self.assertEqual(mixedVolume([[[2,0], [0,2], [4, 5], [4,3]], 
                                     [[2,0], [0,2], [4, 5], [4,3]]]), 9.0)

        # Testing that mixed volume is symmetric in its arguments, expect the
        # same result for the next six statements
        self.assertEqual(mixedVolume(
           [[[6,4,2], [8,-2,4], [4,2,8], [-2,4,0]], 
            [[9,6,3], [12,-3,6], [6,3,12], [-3,6,0]], 
            [[21,14,7], [28,-7,14], [14,7,28], [-7,14,0]]]), 252.0)
        self.assertEqual(mixedVolume(
           [[[9,6,3], [12,-3,6], [6,3,12], [-3,6,0]],
            [[6,4,2], [8,-2,4], [4,2,8], [-2,4,0]],
            [[21,14,7], [28,-7,14], [14,7,28], [-7,14,0]]]), 252.0)
        self.assertEqual(mixedVolume(
           [[[6,4,2], [8,-2,4], [4,2,8], [-2,4,0]],
            [[21,14,7], [28,-7,14], [14,7,28], [-7,14,0]], 
            [[9,6,3], [12,-3,6], [6,3,12], [-3,6,0]]]), 252.0)
        self.assertEqual(mixedVolume(
           [[[9,6,3], [12,-3,6], [6,3,12], [-3,6,0]],
            [[21,14,7], [28,-7,14], [14,7,28], [-7,14,0]],
            [[6,4,2], [8,-2,4], [4,2,8], [-2,4,0]]]), 252.0)
        self.assertEqual(mixedVolume(
           [[[21,14,7], [28,-7,14], [14,7,28], [-7,14,0]],
            [[6,4,2], [8,-2,4], [4,2,8], [-2,4,0]], 
            [[9,6,3], [12,-3,6], [6,3,12], [-3,6,0]]]), 252.0)
        self.assertEqual(mixedVolume(
           [[[21,14,7], [28,-7,14], [14,7,28], [-7,14,0]],
            [[9,6,3], [12,-3,6], [6,3,12], [-3,6,0]],
            [[6,4,2], [8,-2,4], [4,2,8], [-2,4,0]]]), 252.0)
          
        # Testing that mixed volume is multilinear
        # Expect approximately the same result
        body1 = [[1, 4, 2], [16, 3, -9], [4, 0, 2]]
        body2 = [[9, -5, 2], [1, 3, -8], [7, -6, 3]]
        body3 = [[8, 7, 4], [3, -6, 0], [3, 1, 5]]
        body4 = [[5, -4, 2], [3, 1, -5], [0, 9, -4]]
        lambda1 = 2
        lambda2 = 5

        # The Minkowski sum of lambda1 * body1 + lambda2 * body2
        bodyNew = [[47, -17, 14],[7,23,-36], [37,-22,19], 
                  [77,-19,-8], [37,21,-58], [67,-24,-3], 
                  [53,-25,14], [13,15,-36], [43,-30,19]]
            
        self.assertAlmostEqual(mixedVolume([bodyNew, body3, body4]), 
                              lambda1 * mixedVolume([body1, body3, body4]) + 
                              lambda2 * mixedVolume([body2, body3, body4]))
       
        with self.assertRaises(ValueError):
            mixedVolume([[[2,0], [0,2], [4, 6], [4,1]], [[2,0], [4, 5], [4,3,1]]])
          

if __name__ == '__main__':
    unittest.main() 

