# Accuknox Assessment
---
 Assessment Answers

Question 1:
Answer - Django signals are synchronous by default. Signal handlers execute immediately and block the calling code until completion.

Question 2:
Answer - Signal handlers run in the same thread as the code that triggered them. No thread switching occurs.

Question 3:
Answer - Signal handlers execute within the same database transaction as the calling code.

---
## 📝 Rectangle Class Usage

```python
from utils.rectangle import Rectangle

# Create a rectangle
rect = Rectangle(length=10, width=5)

# Iterate over it
for dimension in rect:
    print(dimension)

# Output:
# {'length': 10}
# {'width': 5}

# Use helper methods
print(f"Area: {rect.area()}")        # Output: Area: 50
print(f"Perimeter: {rect.perimeter()}")  # Output: Perimeter: 30
```
