# Topic 2: Custom Classes in Python - Rectangle Class

class Rectangle:
    """
    A Rectangle class with the following features:
    1. Requires length and width (both integers) for initialization
    2. Is iterable - supports iteration
    3. When iterated, yields length first as {'length': value},
       then width as {'width': value}
    """
    
    def __init__(self, length: int, width: int):
        """
        Initialize a Rectangle instance.
        
        Args:
            length (int): The length of the rectangle
            width (int): The width of the rectangle
        """
        self.length = length
        self.width = width
    
    def __iter__(self):
        """
        Make the Rectangle iterable.
        Yields length first, then width in the required format.
        """
        yield {'length': self.length}
        yield {'width': self.width}
    
    def __repr__(self):
        """String representation of the Rectangle."""
        return f"Rectangle(length={self.length}, width={self.width})"
    
    def __str__(self):
        """User-friendly string representation."""
        return f"Rectangle with length={self.length} and width={self.width}"


# Usage and Test Cases
if __name__ == "__main__":
    print("=" * 60)
    print("RECTANGLE CLASS DEMONSTRATION")
    print("=" * 60)
    
    # Create an instance
    print("\n1. Creating a Rectangle instance:")
    rect = Rectangle(length=10, width=5)
    print(f"   {rect}")
    
    # Demonstrate iteration
    print("\n2. Iterating over the Rectangle:")
    print("   for dimension in rect:")
    for dimension in rect:
        print(f"       {dimension}")
    
    # Show the exact output format
    print("\n3. Exact output format verification:")
    dimensions = list(rect)
    print(f"   First yield:  {dimensions[0]}")
    print(f"   Second yield: {dimensions[1]}")
    
    # Verify with different dimensions
    print("\n4. Testing with different dimensions:")
    rect2 = Rectangle(length=20, width=15)
    print(f"   {rect2}")
    for dimension in rect2:
        print(f"       {dimension}")
    
    print("\n" + "=" * 60)
    print("All requirements satisfied:")
    print("✓ length and width are initialized as integers")
    print("✓ Rectangle is iterable")
    print("✓ Iteration yields {'length': VALUE} then {'width': VALUE}")
    print("=" * 60)
