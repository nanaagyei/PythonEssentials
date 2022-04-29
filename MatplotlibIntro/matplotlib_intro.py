# matplotlib_intro.py
"""Python Essentials: Intro to Matplotlib.
<Name> Prince Tuffour
<Class> MTH 520 Methods and Models of Applied Mathematics
<Date> April 28
"""

from statistics import variance
import numpy as np
from matplotlib import pyplot as plt

# Problem 1
def var_of_means(n):
    """Construct a random matrix A with values drawn from the standard normal
    distribution. Calculate the mean value of each row, then calculate the
    variance of these means. Return the variance.

    Parameters:
        n (int): The number of rows and columns in the matrix A.

    Returns:
        (float) The variance of the means of each row.
    """
    dist = np.random.normal(size=(n,n))
    mean_arr = np.mean(dist, axis=1)
    var_arr = np.var(mean_arr)
    return var_arr
    raise NotImplementedError("Problem 1 Incomplete")


def prob1():
    """Create an array of the results of var_of_means() with inputs
    n = 100, 200, ..., 1000. Plot and show the resulting array.
    """
    y = np.array([var_of_means(i) for i in range(100, 1100, 100)])
    return plt.plot(y), plt.show()
    raise NotImplementedError("Problem 1 Incomplete")


# Problem 2
def prob2():
    """Plot the functions sin(x), cos(x), and arctan(x) on the domain
    [-2pi, 2pi]. Make sure the domain is refined enough to produce a figure
    with good resolution.
    """
    x = np.linspace(-2*np.pi, 2*np.pi, 500)
    plt.ion()
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x))
    plt.plot(x, np.tan(x))
    plt.ioff()
    return plt.show()
    raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
def prob3():
    """Plot the curve f(x) = 1/(x-1) on the domain [-2,6].
        1. Split the domain so that the curve looks discontinuous.
        2. Plot both curves with a thick, dashed magenta line.
        3. Set the range of the x-axis to [-2,6] and the range of the
           y-axis to [-6,6].
    """
    x1 = np.linspace(-2, 1, 500)
    f = lambda x: 1/(x-1)

    x2 = np.linspace(1,6, 500)
    plt.ion()
    plt.plot(x1, f(x1), 'm--' , linewidth=4)
    plt.plot(x2, f(x2), 'm--' , linewidth=4)
    plt.xlim(-2,5)
    plt.ylim(-6,6)
    plt.ioff()
    return plt.show()
    raise NotImplementedError("Problem 3 Incomplete")


# Problem 4
def prob4():
    """Plot the functions sin(x), sin(2x), 2sin(x), and 2sin(2x) on the
    domain [0, 2pi].
        1. Arrange the plots in a square grid of four subplots.
        2. Set the limits of each subplot to [0, 2pi]x[-2, 2].
        3. Give each subplot an appropriate title.
        4. Give the overall figure a title.
        5. Use the following line colors and styles.
              sin(x): green solid line.
             sin(2x): red dashed line.
             2sin(x): blue dashed line.
            2sin(2x): magenta dotted line.
    """
    x = np.linspace(0, 2*np.pi, 500)
    ax1 = plt.subplot(221)
    ax1.plot(x, np.sin(x), "g-")
    plt.title("Plot of sin(x)")

    ax2 = plt.subplot(222)
    ax2.plot(x, np.sin(2*x), "r--")
    plt.title("Plot of sin(2x)")

    ax3 = plt.subplot(223)
    ax3.plot(x, 2*np.sin(x), "b--")
    plt.title("Plot of 2sin(x)")

    ax4 = plt.subplot(224)
    ax4.plot(x, 2*np.sin(2*x), "m:")
    plt.title("Plot of 2sin(2x)")
    plt.axis([0, 2*np.pi, -2, 2])
    plt.suptitle("Different variations of sine function")
    return plt.show()
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def prob5():
    """Visualize the data in FARS.npy. Use np.load() to load the data, then
    create a single figure with two subplots:
        1. A scatter plot of longitudes against latitudes. Because of the
            large number of data points, use black pixel markers (use "k,"
            as the third argument to plt.plot()). Label both axes.
        2. A histogram of the hours of the day, with one bin per hour.
            Label and set the limits of the x-axis.
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def prob6():
    """Plot the function f(x,y) = sin(x)sin(y)/xy on the domain
    [-2pi, 2pi]x[-2pi, 2pi].
        1. Create 2 subplots: one with a heat map of f, and one with a contour
            map of f. Choose an appropriate number of level curves, or specify
            the curves yourself.
        2. Set the limits of each subplot to [-2pi, 2pi]x[-2pi, 2pi].
        3. Choose a non-default color scheme.
        4. Add a colorbar to each subplot.
    """
    x = np.linspace(-2*np.pi, 2*np.pi, 200)
    y = x.copy()
    X, Y = np.meshgrid(x, y)
    Z = (np.sin(X)*np.sin(Y))/(X*Y)
    plt.subplot(121)
    plt.pcolormesh(X, Y, Z, cmap="inferno")
    plt.colorbar()

    plt.subplot(122)
    plt.contour(X, Y, Z, 10, cmap="hot")
    plt.colorbar()
    return plt.show()
    raise NotImplementedError("Problem 6 Incomplete")