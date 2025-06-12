import numpy as np
import math
import matplotlib.pyplot as plt


def supportFunction(point, points):
    """
    Find the support function of a polygon with vertices in the array points 
    in a given point. The polygon can be in N dimensions.

    Parameters
    ----------
    point : numpy.array
            the point at which the support function is evaluated.
            
    points : numpy.array
            vertices of the polygon.

    Returns
    ----------
    value : int or float 
        value of the support function in a given point.

    Example of usage
    ----------
    supportFunction(np.array([1, -3]), np.array([[0, 0], [2, 0], [0, 1]]))
    """
    if (np.array(points).size == 0):
        raise ValueError("The array points cannot be empty.")
    maxDotProduct =  -math.inf
    for p in points:
        maxDotProduct = max(maxDotProduct, np.dot(p, point))
    return maxDotProduct


def supportFunctionList(pointsList, points):
    """
    Find the support function of a polygon with vertices in the array 
    points for each point in the array pointsList.

    Parameters
    ----------
    pointsList : numpy.array
                an array of points, the support function is evaluated at each
                point in the array.
            
    points : numpy.array
            vertices of the polygon.

    Returns
    ----------
    value : numpy.array 
        array containing the values of the support function for each point in
        pointsList.

    Example of usage
    ----------
    supportFunctionList(np.array([[1, -3], [1, 2], [1, 3], [0, 6], [-5, 2], 
    [-3, -5], [0, -4], [1, -1]]), np.array([[0, 0], [2, 0], [0, 1]]))
    """
    if (np.array(points).size == 0):
        raise ValueError("The array points cannot be empty.")
    supportFunctionList = []
    for point in pointsList:
        supportFunctionList.append(supportFunction(point, points))
    return np.array(supportFunctionList)


def supportFunctionPlot2D(points, x_interval, fineness=0.1):
    """
    Plot the support function for points in 1D.

    Parameters
    ----------            
    points : numpy.array
            vertices of the polygon.

    x_interval : numpy.array
            endpoints of the x values to plot

    fineness : float, optional
            distance between the x coordinates of two adjacent points 
            which are plotted 

    Returns
    ----------
    fig : matplotlib.figure.Figure instance
        Figure for the plot

    Example of usage
    ----------
    supportFunctionPlot2D(np.array([[0], [1]]), np.array([-10, 10]))
    """

    if (np.array(points).size == 0):
        raise ValueError("The array points cannnot be empty.")
    if (np.array(points).shape[1] != 1):
        raise ValueError("Can only plot for points in 1D.")
    if (len(x_interval) != 2):
        raise ValueError("Interval must have exactly two endpoints.")
    
    fig = plt.figure()
    fig.canvas.manager.set_window_title('Support Function')
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title("Support Function")

    x_cords = []
    
    x = x_interval[0]
    while (x < x_interval[1]):
        x_cords.append(x)
        x += fineness
    y_cords = supportFunctionList(x_cords, points)

    plt.plot(x_cords, y_cords)
    plt.show()

    return fig


def supportFunctionPlot3D(points, x_interval, y_interval, finenessX=0.1, 
                          finenessY=0.1):
    """
    Plot the support function for points in 2D.

    Parameters
    ----------            
    points : numpy.array
            vertices of the polygon.

    x_interval : numpy.array
            endpoints of the x values to plot

    y_interval : numpy.array
            endpoints of the y values to plot

    finenessX : float, optional
            distance between the x coordinates of two adjacent points 
            which are plotted 

    finenessY : float, optional
            distance between the y coordinates of two adjacent points 
            which are plotted 

    Returns
    ----------
    fig : matplotlib.figure.Figure instance
        Figure for the plot

    Example of usage
    ----------
    supportFunctionPlot3D(np.array([[0,0], [2,0], [0,5]]), np.array([-20, 20]), 
    np.array([-10, 10]))
    """
    if (np.array(points).size == 0):
        raise ValueError("The array points cannot be empty.")
    if (np.array(points).shape[1] != 2):
        raise ValueError("Can only plot for points in 2D.")
    if (len(x_interval) != 2 or len(y_interval) != 2):
        raise ValueError("Intervals must have exactly two endpoints.")

    fig = plt.figure()
    fig.canvas.manager.set_window_title('Support Function')
    ax = plt.axes(projection='3d')
    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')
    ax.set_zlabel('z-axis')
    plt.title("Support Function")
    
    x_cords = []
    y_cords = []
    z_cords = []

    x = x_interval[0]
    y = y_interval[0]
    while (x < x_interval[1]):
        x_cords.append(x)
        x += finenessX
    while (y < y_interval[1]):
        y_cords.append(y)
        y += finenessY
    x_cords = np.array(x_cords)
    y_cords = np.array(y_cords)

    # b in y_cords before a in x_cords because of how meshgrid works
    xy_cords = [[a, b] for b in y_cords for a in x_cords]
    
    z_cords = supportFunctionList(xy_cords, points)

    x_cords, y_cords = np.meshgrid(x_cords,y_cords)

    z_cords = np.reshape(z_cords, x_cords.shape)

    ax.plot_surface(x_cords, y_cords, z_cords)
    plt.show()

    return fig
