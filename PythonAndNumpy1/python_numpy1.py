# python_intro.py
"""Python Essentials: Introduction to Python.
<Name>Prince Agyei Tuffour
<Class> MTH 520 Models and Methods of Applied Mathematics
<Date> April 15 2022
"""
import numpy as np

#Problem 1
pi = 3.14159
r = 10
scale = 4/3

V = scale * pi * r**3
print(V)

# #Problem 2
def prob2():
    print("Hello World!")

#Problem 3
def sphere_volume(r):
    """Returns the volume of a sphere for a given radius r
    """
    volume = 4/3 * 3.14159 * r**3
    return volume


# if __name__ == "__main__":
#     print(sphere_volume(r))


#Problem 4
def prob4():
    A = np.array([[3, -1, 4],
                  [1, 5, -9]])
    
    B = np.array([[2, 6, -5, 3],
                  [5, -8, 9, 7],
                  [9, -3, -2, -3]])
    return np.dot(A,B)

#Problem 5
def tax_liability(income):
    first_tax = 0
    second_tax = 0
    third_tax = 0
    if income <= 9785:
        first_tax = 0.1 * income
    elif 9875.01 <= income <= 40125:
        first_tax = 0.1 * 9785
        second_tax = 0.12 * (income - 9785)
    else:
        first_tax = 0.1 * 9875
        second_tax = 0.12 * 30249.99
        third_tax = 0.22 * (income - 40125)
    return first_tax + second_tax + third_tax

#Problem 6
def prob6a():
    A = [i for i in range(1,8)]
    B = list([5]*7)
    A_plus_B = [x+y for x, y in zip(A,B)]
    A_dot_B = sum([x*y for x,y in zip(A,B)])
    scaling = [5*x for x in A]
    return A_dot_B, A_plus_B, scaling

def prob6b():
    A = np.array([1,2,3,4,5,6,7])
    B = np.array([5,5,5,5,5,5,5])
    A_plus_B = A + B
    A_dot_B = np.dot(A,B)
    scaling = 5*A
    return A_dot_B, A_plus_B, scaling


if __name__ == "__main__":
    print(prob6a())