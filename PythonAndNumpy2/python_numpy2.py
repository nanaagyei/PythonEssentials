# python_intro.py
"""Python Essentials: Introduction to Python.
<Name> Prince Agyei Tuffour
<Class> MTH 520 Models and Methods of Applied Mathematics
<Date> April 22
"""
import numpy as np

#Problem 1
def values(a, b, c, d, e):
    print(a, b, c, sep="     ", end=" ")
    print(d, e, sep=" ")

def isolate(a, b, c, d, e):
    return values(a, b, c, d, e)
    raise NotImplementedError("Problem 1 Incomplete")

#Problem 2
def first_half(string):
    if len(string) % 2 == 0:
        return string[:(len(string)/2 +1)]
    else:
        return string[:((len(string)+1)/2)]
    raise NotImplementedError("Problem 2 Incomplete")


def backward(first_string):
    reversed_string = first_string[::-1]
    return reversed_string
    raise NotImplementedError("Problem 2 Incomplete")

#Problem 3
def list_ops():
    entry = ["bear", "ant", "cat", "dog"]
    entry.append("eagle")
    entry[2] = "fox"
    entry.pop(1)
    entry.sort()
    entry.reverse()
    entry[entry.index("eagle")] = "hawk"
    entry.append("hunter")
    return entry
    raise NotImplementedError("Problem 3 Incomplete")

#Problem 4
def alt_harmonic(n):
    """Return the partial sum of the first n terms of the alternating
    harmonic series. Use this function to approximate ln(2).
    """
    series = sum([((-1)**(i+1))/i for i in range(1,n+1)])
    return series
    raise NotImplementedError("Problem 4 Incomplete")


#Problem 5
def prob5(A):
    """Make a copy of 'A' and set all negative entries of the copy to 0.
    Return the copy.

    Example:
        >>> A = np.array([-3,-1,3])
        >>> prob4(A)
        array([0, 0, 3])
    """
    B = np.copy(A)
    index = B < 0
    B[index] = np.zeros(np.size(B[index]))
    return B
    raise NotImplementedError("Problem 5 Incomplete")

#Problem 6
def prob6():
    """Define the matrices A, B, and C as arrays. Return the block matrix
                                | 0 A^T I |
                                | A  0  0 |,
                                | B  0  C |
    where I is the 3x3 identity matrix and each 0 is a matrix of all zeros
    of the appropriate size.
    """
    A = np.array([[0,2,4],[1,3,5]])
    B = np.tril(np.ones(3)*3)
    C = np.diag([-2,-2,-2])
    block1 = np.vstack((np.zeros((3,3)),A, B))
    block2 = np.vstack((A.T,np.zeros((2,2)), np.zeros((3,2))))
    block3 = np.vstack((np.eye(3),np.zeros((2,3)),C))
    block_matrix = np.concatenate([block1,block2,block3], axis=1)
    return block_matrix
    raise NotImplementedError("Problem 6 Incomplete")

#Problem 7
def prob7(A):
    """Divide each row of 'A' by the row sum and return the resulting array.

    Example:
        >>> A = np.array([[1,1,0],[0,1,0],[1,1,1]])
        >>> prob6(A)
        array([[ 0.5       ,  0.5       ,  0.        ],
               [ 0.        ,  1.        ,  0.        ],
               [ 0.33333333,  0.33333333,  0.33333333]])
    """
    b = np.sum(A, axis=1)
    row_division = b.reshape(np.size(b), 1)
    row_stochastic_matrix = A/row_division
    return row_stochastic_matrix
    raise NotImplementedError("Problem 7 Incomplete")

#Problem 8
def prob8():
    """Given the array stored in grid.npy, return the greatest product of four
    adjacent numbers in the same direction (up, down, left, right, or
    diagonally) in the grid.
    """
    grip = np.load("grip.npy")
    ss = np.array([[int(x) for x in grip.split()][i:i+20] for i in range(0,400,20)]).reshape(20, 20)


    #check right: row: 1 thru 20 (index 0:19); columns: 1 thru 16 (index 0:15)
    mr = max(np.prod(ss[i,j:j+4]) for i in range(20) for j in range(16))

    #check down: row: 1 thru 16 (index 0:15); columns: 1 thru 20 (index 0:19)
    mc = max(np.prod(ss[i:i+4,j]) for i in range(16) for j in range(20))

    #check right-down-diagonal: row: 1 thru 16 (index 0:15); columns: 1 thru 16 (index 0:15). row,col increments by 1 to go right-down-diagonal 
    mx = max(np.prod([ss[i+k,j+k] for k in range(4)]) for i in range(16) for j in range(16))

    #check left-down-diagonal: row: 1 thru 20 (index 0:19); columns: 4 thru 20 (index 3:19). row increments by 1 and col decrements by 1 to go right-down-diagonal
    my = max(np.prod([ss[i+k,j-k] for k in range(4)]) for i in range(16) for j in range(3,20))

    ans = max([mr,mc,mx,my])

    return ans
    raise NotImplementedError("Problem 8 Incomplete")
