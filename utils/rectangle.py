"""
Rectangle class implementation for Assessment Topic 2.

Requirements:
1. Requires length:int and width:int to be initialized
2. Is iterable
3. When iterated, yields {'length': VALUE} first, then {'width': VALUE}
"""


class Rectangle:
    """
    A Rectangle class that supports iteration.
    
    This class implements the iterator protocol to make Rectangle
    instances iterable. When iterating over a Rectangle, it yields
    the length first, then the width, each as a dictionary.
    
    Attributes:
        length (int): The length of the rectangle
        width (int): The width of the rectangle
    
    Example:
        >>> rect = Rectangle(10, 5)
        >>> for dimension in rect:
        ...     print(dimension)
        {'length': 10}
        {'width': 5}
    """
    
    def __init__(self, length: int, width: int):
        """
        Initialize a Rectangle instance.
        
        Args:
            length (int): The length of the rectangle
            width (int): The width of the rectangle
        
        Raises:
            TypeError: If length or width is not an integer
        """
        if not isinstance(length, int) or not isinstance(width, int):
            raise TypeError("Both length and width must be integers")
        
        self.length = length
        self.width = width
    
    def __iter__(self):
        """
        Make the Rectangle iterable.
        
        Yields dimensions as dictionaries. First yields the length,
        then yields the width.
        
        Yields:
            dict: First {'length': self.length}, then {'width': self.width}
        """
        yield {'length': self.length}
        yield {'width': self.width}
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"Rectangle(length={self.length}, width={self.width})"
    
    def __str__(self) -> str:
        """User-friendly string representation."""
        return f"Rectangle {self.length}x{self.width}"
    
    def area(self) -> int:
        """Calculate the area of the rectangle."""
        return self.length * self.width
    
    def perimeter(self) -> int:
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.length + self.width)
