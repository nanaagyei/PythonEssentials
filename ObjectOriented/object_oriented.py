# object_oriented.py
"""Python Essentials: Object Oriented Programming.
<Name>
<Class>
<Date>
"""

from math import sqrt


class Backpack:
    """A Backpack object class. Has a name, color, max_size and a list of contents.

    Attributes:
        name (str): the name of the backpack's owner.
        contents (list): the contents of the backpack.
        color (str): the color of the backpack.
        max_size (int): maximum number of items the backpack can hold.
    """

    # Problem 1: Modify __init__() and put(), and write dump().
    def __init__(self, name, color, max_size=5):
        """Set the name, color and maximum size and initialize an empty list of contents.

        Parameters:
            name (str): the name of the backpack's owner.
            color (str): the color of the backpack.
            max_size (int): maximum number of items the backpack can hold.
        """
        self.name = name
        self.contents = []
        self.color = color
        self.max_size = max_size

    def put(self, item):
        """Add an item to the backpack's list of contents. 
           Does not add an item if the content if max_size is exceeded.
        """
        self.contents.append(item)
        if len(self.contents) > self.max_size:
            print("No Room!")

    def take(self, item):
        """Remove an item from the backpack's list of contents."""
        self.contents.remove(item)
    
    def dump(self):
        """Clears the list of content."""
        self.contents.clear()
    # Magic Methods -----------------------------------------------------------

    # Problem 3: Write __eq__() and __str__().
    def __add__(self, other):
        """Add the number of contents of each Backpack."""
        return len(self.contents) + len(other.contents)

    def __lt__(self, other):
        """Compare two backpacks. If 'self' has fewer contents
        than 'other', return True. Otherwise, return False.
        """
        return len(self.contents) < len(other.contents)
    
    def __eq__(self, other):
        """Compare two backpacks. If 'self' has the same name,
        color, and number of contents as 'other', return True.
        Otherwise, return False.
        """
        return (self.name == other.name) and (self.color == other.color) and (len(self.contents) == len(other.contents))
    
    def __str__(self):
        return "Owner: \t " + self.name + "\n" + "Color: \t " + self.color + "\n" + "Size: \t " + str(len(self.contents)) + "\n" + "Max Size: " + str(self.max_size) + "\n" + "Contents: " + str(self.contents)


# An example of inheritance. You are not required to modify this class.
class Knapsack(Backpack):
    """A Knapsack object class. Inherits from the Backpack class.
    A knapsack is smaller than a backpack and can be tied closed.

    Attributes:
        name (str): the name of the knapsack's owner.
        color (str): the color of the knapsack.
        max_size (int): the maximum number of items that can fit inside.
        contents (list): the contents of the backpack.
        closed (bool): whether or not the knapsack is tied shut.
    """
    def __init__(self, name, color):
        """Use the Backpack constructor to initialize the name, color,
        and max_size attributes. A knapsack only holds 3 item by default.

        Parameters:
            name (str): the name of the knapsack's owner.
            color (str): the color of the knapsack.
            max_size (int): the maximum number of items that can fit inside.
        """
        Backpack.__init__(self, name, color, max_size=3)
        self.closed = True

    def put(self, item):
        """If the knapsack is untied, use the Backpack.put() method."""
        if self.closed:
            print("I'm closed!")
        else:
            Backpack.put(self, item)

    def take(self, item):
        """If the knapsack is untied, use the Backpack.take() method."""
        if self.closed:
            print("I'm closed!")
        else:
            Backpack.take(self, item)

    def weight(self):
        """Calculate the weight of the knapsack by counting the length of the
        string representations of each item in the contents list.
        """
        return sum(len(str(item)) for item in self.contents)


# Problem 2: Write a 'Jetpack' class that inherits from the 'Backpack' class.

class Jetpack(Backpack):
    """A Jetpack object class. Inherits from the Backpack class.
    A Jetpack is a type of Backpack and can have fuel.

    Attributes:
        name (str): the name of the knapsack's owner.
        color (str): the color of the knapsack.
        max_size (int): the maximum number of items that can fit inside.
        contents (list): the contents of the backpack.
        fuel (int): amount of fuel.
    """

    def __init__(self, name, color, max_size=2, fuel=10):
        """Uses the Backpack constructor to initialize the same attributes (name, color, and max_size).
           Initializes a new attribute that display the amount of fuel in Jetpack
        
        Parameters:
            name (str): the name of the knapsack's owner.
            color (str): the color of the knapsack.
            max_size (int): the maximum number of items that can fit inside.
            fuel (int): amount of fuel.
        """
        Backpack.__init__(self, name, color, max_size)
        self.fuel = fuel
    
    def fly(self, fuel_burned):
        """Burns an amount of fuel when Jetpack flies. If fuel burned exceeds amount of fuel remains,
           Jetpack does not fly
        """
        if (self.fuel - fuel_burned) < 0:
            print("Not enough fuel!")
        else:
            self.fuel  = self.fuel - fuel_burned
    
    def dump(self):
        self.contents.clear()
        self.fuel = 0


# Problem 4: Write a 'ComplexNumber' class.

class ComplexNumber:
    """A Complex number object class. Performs operations on complex numbers.
    Accepts real and imaginary parts of complex numbers to perform basic 
    complex operations.

    Attributes:
        real (float): the real part of the complex number
        imag (float): the imaginary part of the complex number.
    """

    def __init__(self, real, imag):
        """Set the constructor to initialize the real and imaginary parts

        Parameters:
            real (float): the real part of the complex number
            imag (float): the imaginary part of the complex number.
        """

        self.real = real
        self.imag = imag

    def conjugate(self):
        """Returns the conjugate of a complex number. Returns complex number
        as a ComplexNumber object.
        """
        return ComplexNumber(self.real, -self.imag)

    def __str__(self):
        """Prints the complex number if imaginary is greater than or less than 0.
        """
        if self.imag >= 0:
            return "(" + str(self.real) + "+" + str(self.imag) + "j" + ")"
        return "(" + str(self.real) + "-" + str(-self.imag) + "j" + ")"
    
    def __abs__(self):
        """Returns the magnitude of the complex number.
        """
        return sqrt((self.real)**2 + (self.imag)**2)
    
    def __eq__(self, other):
        """Determines if two ComplexNumber objects are objects. Returns True if
        real and imag parts are equal.
        """

        if self.real == other.real and self.imag == other.imag:
            return True
        return False
    
    def __add__(self, other):
        """Adds two ComplexNumber objects to produce a new ComplexNumber object.
        Adds the real parts and imag parts.
        """

        return ComplexNumber(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        """Substracts two ComplexNumber objects. Substracts the real parts and imag parts.
        """

        return ComplexNumber(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other):
        """Performs complex multiplication on two ComplexNumber objects to produce a new
        ComplexNumber object. 
        """

        return ComplexNumber(((self.real) * (other.real) - (self.imag) * (other.imag)),((self.real) * (other.imag) + (self.imag) * (other.real)))
    

    def __truediv__(self, other):
        """Performs complex division on two ComplexNumber objects to obtain a new 
        ComplexNumber object.
        """

        a = self.real
        b = self.imag
        c = other.real
        d = other.imag

        return ComplexNumber(((a * c) + (b * d))/(c**2 - d**2),((b * c) - (a * d))/(c**2 - d**2))


def test_ComplexNumber(a, b):
    py_cnum, my_cnum = complex(a, b), ComplexNumber(a, b)
    # Validate the constructor.
    if my_cnum.real != a or my_cnum.imag != b:
        print("__init__() set self.real and self.imag incorrectly")
    # Validate conjugate() by checking the new number's imag attribute.
    if py_cnum.conjugate().imag != my_cnum.conjugate().imag:
        print("conjugate() failed for", py_cnum)
    # Validate __str__().
    if str(py_cnum) != str(my_cnum):
        print("__str__() failed for", py_cnum)

