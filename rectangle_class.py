class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    
    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}
    
    def __repr__(self):
        return f"Rectangle(length={self.length}, width={self.width})"
    
    def __str__(self):
        return f"Rectangle with length={self.length} and width={self.width}"


# Usage and Test Cases
if __name__ == "__main__":
    
    rect = Rectangle(length=10, width=5)
    print(f"   {rect}")
    
    print("   for dimension in rect:")
    for dimension in rect:
        print(f"       {dimension}")
    
    dimensions = list(rect)
    print(f"   First :  {dimensions[0]}")
    print(f"   Second : {dimensions[1]}")
    
    rect2 = Rectangle(length=20, width=15)
    print(f"   {rect2}")
    for dimension in rect2:
        print(f"       {dimension}")
