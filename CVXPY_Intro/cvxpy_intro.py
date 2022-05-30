# cvxpy_intro.py
"""Volume 2: Intro to CVXPY.
<Name> Prince Tuffour
<Class> MTH 520 Model & Methods of Applied Mathematics
<Date> May 26
"""

import cvxpy as cp
import numpy as np


def prob1():
    """Solve the following convex optimization problem:

    minimize        2x + y + 3z
    subject to      x  + 2y         <= 3
                         y   - 4z   <= 1
                    2x + 10y + 3z   >= 12
                    x               >= 0
                          y         >= 0
                                z   >= 0

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    x = cp.Variable(3, nonneg=True)
    c = np.array([2, 1, 3])
    objective = cp.Minimize(c.T @ x)

    #constraints
    A = np.array([1, 2, 0])
    B = np.array([0, 1, -4])
    C = np.array([2, 10, 3])
    P = np.eye(3)

    constraints = [A @ x <= 3, B @ x <= 1, C @ x >= 12, P @ x >= 0]
    problem = cp.Problem(objective, constraints)
    
    D = problem.solve()
    return x.value, D
    raise NotImplementedError("Problem 1 Incomplete")


# Problem 2
def l1Min(A, b):
    """Calculate the solution to the optimization problem

        minimize    ||x||_1
        subject to  Ax = b

    Parameters:
        A ((m,n) ndarray)
        b ((m, ) ndarray)

    Returns:
        The optimizer x (ndarray)
        The optimal value (float)
    """
    m,n = A.shape
    x = cp.Variable(n, nonneg=True)
    objective = cp.Minimize(cp.norm(x, 1))

    constraints = [A @ x == b]

    problem  = cp.Problem(objective, constraints)

    C = problem.solve()

    return x.value, C
    raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
def prob3():
    """Solve the transportation problem by converting the last equality constraint
    into inequality constraints.

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    x = cp.Variable(6, nonneg=True)
    c = np.array([4, 7, 6, 8, 8, 9])
    objective = cp.Minimize(c.T @ x)

    #constraints
    A = np.array([1, 1, 0, 0, 0, 0])
    B = np.array([0, 0, 1, 1, 0, 0])
    C = np.array([0, 0, 0, 0, 1, 1])
    D = np.array([1, 0, 1, 0, 1, 0])
    E = np.array([0, 1, 0, 1, 0, 1])
    P = np.eye(6)

    constraints = [A @ x == 7, B @ x == 2, C @ x == 4, D @ x == 5, E @ x == 8, P @ x >= 0]

    problem = cp.Problem(objective, constraints)
    primal = problem.solve()

    return x.value, primal
    raise NotImplementedError("Problem 3 Incomplete")


# Problem 4
def prob4():
    """Find the minimizer and minimum of

    g(x,y,z) = (3/2)x^2 + 2xy + xz + 2y^2 + 2yz + (3/2)z^2 + 3x + z

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    Q = np.array([[3, 2, 1],
                  [2, 4, 2],
                  [1, 2, 3]])
    r = np.array([3, 0, 1])
    x = cp.Variable(3)
    objective = cp.Minimize(0.5 * cp.quad_form(x, Q) + r.T @ x)
    problem = cp.Problem(objective)
    val = problem.solve()

    return x.value, val
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def prob5(A, b):
    """Calculate the solution to the optimization problem
        minimize    ||Ax - b||_2
        subject to  ||x||_1 == 1
                    x >= 0
    Parameters:
        A ((m,n), ndarray)
        b ((m,), ndarray)
        
    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    m, n = A.shape
    x = cp.Variable(n, nonneg=True)
    objective = cp.Minimize(cp.norm(A @ x - b))

    l1_norm = np.ones(n)
    P = np.eye(n)

    constraint = [l1_norm @ x == 1, P @ x >= 0]

    problem = cp.Problem(objective, constraint)
    C = problem.solve()

    return x.value, C
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def prob6():
    """Solve the college student food problem. Read the data in the file 
    food.npy to create a convex optimization problem. The first column is 
    the price, second is the number of servings, and the rest contain
    nutritional information. Use cvxpy to find the minimizer and primal 
    objective.
    
    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """	 
    raise NotImplementedError("Problem 6 Incomplete")



if __name__ == "__main__":
    print("#"*20 + "Problem 1" + "#"*20)
    print(prob1())

    A = np.array([[1, 2, 1, 1],
                  [0, 3, -2, -1]])
    
    b = np.array([7, 4])
    print("#"*20 + "Problem 2" + "#"*20)
    print(l1Min(A, b))
    print("#"*20 + "Problem 3" + "#"*20)
    print(prob3())
    print("#"*20 + "Problem 4" + "#"*20)
    print(prob4())
    print("#"*20 + "Problem 5" + "#"*20)
    print(prob5(A, b))