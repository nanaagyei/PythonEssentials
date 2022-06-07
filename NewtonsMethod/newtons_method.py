# newtons_method.py
"""Volume 1: Newton's Method.
<Name> Prince Tuffour
<Class> MTH 520 Models and Methods of Applied Mathematics
<Date> June 6, 2022
"""
import math
import numpy as np
import matplotlib.pyplot as plt


# Problems 1, 3, and 5
def newton(f, x0, Df, tol=1e-5, maxiter=15, alpha=0.4):
    """Use Newton's method to approximate a zero of the function f.

    Parameters:
        f (function): a function from R^n to R^n (assume n=1 until Problem 5).
        x0 (float or ndarray): The initial guess for the zero of f.
        Df (function): The derivative of f, a function from R^n to R^(nxn).
        tol (float): Convergence tolerance. The function should returns when
            the difference between successive approximations is less than tol.
        maxiter (int): The maximum number of iterations to compute.
        alpha (float): Backtracking scalar (Problem 3).

    Returns:
        (float or ndarray): The approximation for a zero of f.
        (bool): Whether or not Newton's method converged.
        (int): The number of iterations computed.
    """
    count = 0
    for k in range(maxiter):
        x1 = x0 - alpha * (f(x0)/Df(x0))
        if abs(x1-x0) < tol:
            break
        x0 = x1
        count += 1
    if count < maxiter:
        return x0, True, count
    return x0, False, count
    raise NotImplementedError("Problem 1 Incomplete")


# Problem 2
def prob2(N1, N2, P1, P2):
    """Use Newton's method to solve for the constant r that satisfies

                P1[(1+r)**N1 - 1] = P2[1 - (1+r)**(-N2)].

    Use r_0 = 0.1 for the initial guess.

    Parameters:
        P1 (float): Amount of money deposited into account at the beginning of
            years 1, 2, ..., N1.
        P2 (float): Amount of money withdrawn at the beginning of years N1+1,
            N1+2, ..., N1+N2.
        N1 (int): Number of years money is deposited.
        N2 (int): Number of years money is withdrawn.

    Returns:
        (float): the value of r that satisfies the equation.
    """
    f = lambda r: P1 * ((1+r)**N1 - 1) - P2 * (1 - (1+r)**(-N2))
    Df = lambda r: N1 * P1 * (1+r)**(N1-1) - N2* P2 * (1+r)**(-N2-1)
    r0 = 0.1
    maxiter = 15
    tol = 1e-5
    for k in range(maxiter):
        r1 = r0 - (f(r0)/Df(r0))
        if abs(r1-r0) < tol:
            break
        r0 = r1
    return r0
    raise NotImplementedError("Problem 2 Incomplete")


# Problem 4
def optimal_alpha(f, x0, Df, tol=1e-5, maxiter=15):
    """Run Newton's method for various values of alpha in (0,1].
    Plot the alpha value against the number of iterations until convergence.

    Parameters:
        f (function): a function from R^n to R^n (assume n=1 until Problem 5).
        x0 (float or ndarray): The initial guess for the zero of f.
        Df (function): The derivative of f, a function from R^n to R^(nxn).
        tol (float): Convergence tolerance. The function should returns when
            the difference between successive approximations is less than tol.
        maxiter (int): The maximum number of iterations to compute.

    Returns:
        (float): a value for alpha that results in the lowest number of
            iterations.
    """
    a = np.linspace(0, 1, 100)[1:]
    counts = np.array([])
    for alpha in a:
        x, bool, count = newton(f, x0, Df, tol=1e-5, maxiter=15, alpha=alpha)
        counts = np.append(counts, count)
    least_iter = a[np.argmin(counts)]
    plt.plot(a, counts)
    plt.show()
    return least_iter
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 6
def prob6():
    """Consider the following Bioremediation system.

                              5xy − x(1 + y) = 0
                        −xy + (1 − y)(1 + y) = 0

    Find an initial point such that Newton’s method converges to either
    (0,1) or (0,−1) with alpha = 1, and to (3.75, .25) with alpha = 0.55.
    Return the intial point as a 1-D NumPy array with 2 entries.
    """
    raise NotImplementedError("Problem 6 Incomplete")


# Problem 7
def plot_basins(f, Df, zeros, domain, res=1000, iters=15):
    """Plot the basins of attraction of f on the complex plane.

    Parameters:
        f (function): A function from C to C.
        Df (function): The derivative of f, a function from C to C.
        zeros (ndarray): A 1-D array of the zeros of f.
        domain ([r_min, r_max, i_min, i_max]): A list of scalars that define
            the window limits and grid domain for the plot.
        res (int): A scalar that determines the resolution of the plot.
            The visualized grid has shape (res, res).
        iters (int): The exact number of times to iterate Newton's method.
    """
    raise NotImplementedError("Problem 7 Incomplete")


if __name__ == "__main__":
    # f = lambda x: math.exp(x) - 2
    # Df = lambda x: math.exp(x)
    # print(newton(f, 2, Df))

    # print(prob2(30, 20, 2000, 8000))

    f = lambda x: np.sign(x) * np.power(np.abs(x), 1./3)

    Df = lambda x: (1./3) * np.power(np.abs(x), -2./3)
    print(optimal_alpha(f,0.01, Df))
