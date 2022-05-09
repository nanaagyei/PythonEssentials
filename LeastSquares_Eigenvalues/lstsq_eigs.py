# lstsq_eigs.py
"""Volume 1: Least Squares and Computing Eigenvalues.
<Name>
<Class>
<Date>
"""

# (Optional) Import functions from your QR Decomposition lab.
# import sys
# sys.path.insert(1, "../QR_Decomposition")
# from qr_decomposition import qr_gram_schmidt, qr_householder, hessenberg

import numpy as np
from matplotlib import pyplot as plt
from scipy import linalg as la

# Problem 1
def least_squares(A, b):
    """Calculate the least squares solutions to Ax = b by using the QR
    decomposition.

    Parameters:
        A ((m,n) ndarray): A matrix of rank n <= m.
        b ((m, ) ndarray): A vector of length m.

    Returns:
        x ((n, ) ndarray): The solution to the normal equations.
    """
    Q, R = la.qr(A, mode="economic")
    b1 = (Q.T).dot(b)
    x = la.solve_triangular(R, b1)
    return x
    raise NotImplementedError("Problem 1 Incomplete")

# Problem 2
def line_fit():
    """Find the least squares line that relates the year to the housing price
    index for the data in housing.npy. Plot both the data points and the least
    squares line.
    """
    housing = np.load("housing.npy")
    x, y = housing[:, 0], housing[:, 1]
    X = np.vstack((x, np.ones(x.shape))).T
    a, b = least_squares(X, y)
    plt.plot(x, y, "k*", label="Data Points")
    plt.plot(x, a * x + b, label="Line fit")
    plt.legend(loc="upper left")
    return plt.show()
    raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
def polynomial_fit():
    """Find the least squares polynomials of degree 3, 6, 9, and 12 that relate
    the year to the housing price index for the data in housing.npy. Plot both
    the data points and the least squares polynomials in individual subplots.
    """
    housing = np.load("housing.npy")
    x1, y = housing[:, 0], housing[:, 1]
    x_axis = np.linspace(0, 17, 200)
    # polynomial of degree 3
    A = np.vander(x1, 4)
    x = la.lstsq(A, y)[0]
    f = np.poly1d(x)
    plt.plot(x1, y, "k*", label="Data Points")
    plt.plot(x_axis, f(x_axis), "b-", label="Deg 3")

    #Polynomial of degree 6
    B = np.vander(x1, 7)
    v = la.lstsq(B, y)[0]
    g = np.poly1d(v)
    plt.plot(x_axis, g(x_axis), "g--", label="Deg 6")

    #Polynomial of degree 9
    C = np.vander(x1, 10)
    w = la.lstsq(C, y)[0]
    h = np.poly1d(w)
    plt.plot(x_axis, h(x_axis), "r-", label="Deg 9")

    #Polynomial of degree 12
    D = np.vander(x1, 13)
    z = la.lstsq(D, y)[0]
    p = np.poly1d(z)
    plt.plot(x_axis, p(x_axis), "k-", label="Deg 12")

    plt.legend(loc="upper left")
    return plt.show()
    raise NotImplementedError("Problem 3 Incomplete")


def plot_ellipse(a, b, c, d, e):
    """Plot an ellipse of the form ax^2 + bx + cxy + dy + ey^2 = 1."""
    theta = np.linspace(0, 2*np.pi, 200)
    cos_t, sin_t = np.cos(theta), np.sin(theta)
    A = a*(cos_t**2) + c*cos_t*sin_t + e*(sin_t**2)
    B = b*cos_t + d*sin_t
    r = (-B + np.sqrt(B**2 + 4*A)) / (2*A)

    plt.plot(r*cos_t, r*sin_t)
    plt.gca().set_aspect("equal", "datalim")

# Problem 4
def ellipse_fit():
    """Calculate the parameters for the ellipse that best fits the data in
    ellipse.npy. Plot the original data points and the ellipse together, using
    plot_ellipse() to plot the ellipse.
    """
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def power_method(A, N=20, tol=1e-12):
    """Compute the dominant eigenvalue of A and a corresponding eigenvector
    via the power method.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The maximum number of iterations.
        tol (float): The stopping tolerance.

    Returns:
        (float): The dominant eigenvalue of A.
        ((n,) ndarray): An eigenvector corresponding to the dominant
            eigenvalue of A.
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def qr_algorithm(A, N=50, tol=1e-12):
    """Compute the eigenvalues of A via the QR algorithm.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The number of iterations to run the QR algorithm.
        tol (float): The threshold value for determining if a diagonal S_i
            block is 1x1 or 2x2.

    Returns:
        ((n,) ndarray): The eigenvalues of A.
    """
    raise NotImplementedError("Problem 6 Incomplete")

if __name__ == "__main__":
    polynomial_fit()