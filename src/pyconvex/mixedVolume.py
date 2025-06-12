import numpy as np
import math
from scipy.spatial import ConvexHull
from itertools import permutations, product


def findMinkowskiSum(bodies, lambdas):
    """
    Find the volume of the Minkowski sum of the bodies where the bodies are 
    scaled by the corresponding value in lambdas.

    Parameters
    ----------
    bodies : list of n lists containing points in n dimensions
            list of points which make each of the n bodies.

    lambdas : list of floats
            values which the bodies are scaled by.

    Returns
    ----------
    value : float
        volume of the Minkowksi sum.

    Example of usage
    ----------
    findMinkowskiSum([[[2, 3], [1, 5], [6, 7]], 
    [[1, 3], [8, 9], [-1, 4]]], [1, 1])
    """
    minkowskiSumBodies = []

    # Find all possible products of points
    products = list(product(*bodies))
    for prod in products:
        minkowskiSumBodies.append(np.matmul(lambdas, np.array(prod)))
    try:
        minkowskiConvexHull = ConvexHull(np.array(minkowskiSumBodies))
    except:
        # The volume is 0 if the convex hull is not well defined
        return 0
    
    # Find the volume of the convex hull minkowskiConvexHull
    minkowskiSumEndpoints = []
    for i in minkowskiConvexHull.vertices:
        minkowskiSumEndpoints.append(minkowskiConvexHull.points[i])
    return ConvexHull(minkowskiSumEndpoints).volume

def mixedVolume(bodies):
    """
    Find the mixed volume of n convex bodies which are in R^n.

    Each of the n bodies is a convex, nonempty, compact subset of R^n.

    Assume that the number of bodies is the same as the dimension which each 
    point of the bodies is in.

    See equation (5.20) on p. 280 in Convex Bodies: The Brunn-Minkowski Theory 
    by Rolf Schneider (Second Expanded Edition).
    
    Parameters
    ----------
    bodies : list of n lists containing points in n dimensions
            list of points which make each of the n bodies.

    Returns
    ----------
    value : float
        mixed volume of the bodies.

    Example of usage
    ----------
    mixedVolume([[[0,0], [1,0], [0,2], [1,2]], [[0,0], [3,0], [0,4], [3,4]]])
    """
    n = len(bodies)

    # Check that there are n bodies with points in R^n
    for body in bodies:
        for point in body:
            if (len(point) != n):
                raise ValueError("There need to be n bodies and all points " \
                "need to be in R^n.")

    mixedVolume = 0

    for k in range(1, n+1):
        lambdas = []
        for _ in range(k):
            lambdas.append(1)
        for _ in range(n - k):
            lambdas.append(0)
        lambdas_permutations = list(set(permutations(lambdas, n)))
        valueI = 0
        for lambdas in lambdas_permutations:
            valueI += findMinkowskiSum(bodies, lambdas)
        mixedVolume += (-1) ** (n + k) * valueI
    return mixedVolume / math.factorial(n)

