import numpy as np
from supportFunction import *

# Testing the function supportFunction
# Expect -4
print(supportFunction(np.array([-4]), np.array([[1], [8]])))
# Expect 2 
print(supportFunction(np.array([1, -3]), np.array([[0, 0], [2, 0], [0, 1]]))) 
# Expect 43
print(supportFunction(np.array([5, 2]), np.array([[3, 0], [0, 1], [2, 5], 
                                                  [5, 6], [7, 4], [6, 1]])))
# Expect 45
print(supportFunction(np.array([3, -2, 5]), np.array([[1, 0, 2], [5, 7, 6], 
                                                      [8, 2, 5], [6, 7, 1], 
                                                      [-5, 3, 0]])))

# Testing the function supportFunctionList
# Expect [2, 2, 3, 6, 2, 0, 0, 2]
print(supportFunctionList(np.array([[1, -3], [1, 2], [1, 3], [0, 6], [-5, 2], 
                                    [-3, -5], [0, -4], [1, -1]]), 
                                    np.array([[0, 0], [2, 0], [0, 1]]))) 

# Testing the function supportFunctionPlot2D
# Expect a 2d graph where y = 0 if x<0 and y = x if x>=0
supportFunctionPlot2D(np.array([[0], [1]]), np.array([-10, 10]))

# Testing the function supportFunctionPlot3D
# Expect a 3d graph where z=0 if x<0 and y<0, z=2x if x>=0 and y<=0.4x and
# z=5y if y>=0 and y > 0.4x
supportFunctionPlot3D(np.array([[0,0], [2,0], [0,5]]), np.array([-20, 20]), 
                      np.array([-10, 10])) 