# standard_library.py
"""Python Essentials: The Standard Library.
<Name>Prince Agyei Tuffour
<Class> MTH 520 Models and Methods of Applied Mathematics
<Date> April 15
"""
import calculator
from math import sqrt
from itertools import chain, combinations
import box
import sys, time, random

# Problem 1
def prob1(L):
    """Return the minimum, maximum, and average of the entries of L
    (in that order).
    """
    return min(L), max(L), (sum(L)/len(L))
    raise NotImplementedError("Problem 1 Incomplete")


# Problem 2
def prob2():
    """Determine which Python objects are mutable and which are immutable.
    Test numbers, strings, lists, tuples, and sets. Print your results.
    """
    number = 5
    new_number = number
    new_number = 6
    print(number == new_number)
    name = "Prince"
    new_name = name
    new_name = "Price"
    print(name == new_name)
    elements = [1, 2, "food", "school", 5.0]
    elements_1 = elements
    elements_1[1] = "graduate"
    print(elements == elements_1)
    my_tuple = (3, 1, 5, 3)
    my_tuple_1 = my_tuple
    my_tuple_1 += (1,)
    print(my_tuple == my_tuple_1)
    my_set = {3, 9, 0, 1}
    my_new_set = my_set
    my_new_set = {3, 9, 0}
    print(my_new_set == my_set)
    return "list is the only mutable object type. int, str, tuple, and set are all immutable object types"
    raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
def hypot(a, b):
    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any functions other than sum(), product() and sqrt that are 
    imported from your 'calculator' module.

    Parameters:
        a: the length one of the sides of the triangle.
        b: the length the other non-hypotenuse side of the triangle.
    Returns:
        The length of the triangle's hypotenuse.
    """
    return sqrt(calculator.sum(calculator.product(a,a),calculator.product(b,b)))
    raise NotImplementedError("Problem 3 Incomplete")


# Problem 4
def power_set(A):
    """Use itertools to compute the power set of A.

    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.

    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    if A == None:
        return set()
    else:
        subsets = list(A)
        return chain.from_iterable(combinations(subsets, r) for r in range(1, len(subsets)+1))
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5: Implement shut the box.
def shut_the_box(player, timelimit):
    """Play a single game of shut the box."""
    numbers = [i for i in range(1, 10)]
    while numbers != []:
        print("Numbers left: ", numbers)
        input("Please press enter to roll the dice: ")
        rolls = [random.randint(1,6), random.randint(1,6)] #Stores a list of two random values between 1 and 6, inclusive
        if sum(numbers) <= 6:
            roll = random.choice(rolls)
            print("Roll: ", roll)
        else:
            roll = sum(rolls)
            print("Roll: ", roll)
        if box.isvalid(roll, numbers) == True:
            eliminate = input("Numbers to elimiate: ")
            while box.parse_input(eliminate, numbers) == [] or box.isvalid(roll, numbers) == False:
                eliminate = input("Please enter a valid input (Please separate with space): ")
            else:
                numbers = [x for x in numbers if x not in box.parse_input(eliminate, numbers)]
        else:
            print("Game over!")
            print("Score for " + str(player) + ": ", sum(numbers), " points")
            print("Time played: ")
            print("Better luck next time")
    else:
        print("Score for " + str(player) + ": ", sum(numbers), " points")
        print("Time played: ")
        print("Congratulations!! You shut the box")

if (len(sys.argv) != 3):
        print("System failure! Unable to start game. Please enter exactly three arguments including file name, player name, and time limit.")
else:
    shut_the_box(sys.argv[1], sys.argv[2])