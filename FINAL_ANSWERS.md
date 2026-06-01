# ACCUKNOX DJANGO TRAINEE ASSESSMENT - FINAL ANSWERS

## SUBMISSION FORMAT: Django Project Structure

---

## TOPIC 1: DJANGO SIGNALS

### Question 1: By default, are django signals executed synchronously or asynchronously?

**ANSWER:** Synchronously

**PROOF CODE:**
```python
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

class TestModel(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        app_label = 'assessment_app'

@receiver(post_save, sender=TestModel)
def test_signal_handler(sender, instance, created, **kwargs):
    print(f"Signal handler started at: {time.time()}")
    time.sleep(2)
    print(f"Signal handler ended at: {time.time()}")

# Main execution
start = time.time()
print(f"Before save: {start}")
TestModel.objects.create(name="Test")
print(f"After save: {time.time()}")
print(f"Total time: {time.time() - start}")

# If signals were async, this would finish in <0.1s
# Since it takes ~2 seconds, signals are SYNCHRONOUS
```

**LOGIC:** The signal handler executes immediately and blocks until completion. The time elapsed proves execution is synchronous (blocking), not asynchronous (non-blocking).

---

### Question 2: Do django signals run in the same thread as the caller?

**ANSWER:** Yes

**PROOF CODE:**
```python
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

class TestModel(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        app_label = 'assessment_app'

main_thread_id = threading.current_thread().ident

@receiver(post_save, sender=TestModel)
def test_signal_handler(sender, instance, created, **kwargs):
    handler_thread_id = threading.current_thread().ident
    print(f"Main thread ID: {main_thread_id}")
    print(f"Handler thread ID: {handler_thread_id}")
    print(f"Same thread: {main_thread_id == handler_thread_id}")
    assert main_thread_id == handler_thread_id

# Trigger signal
TestModel.objects.create(name="Test")
# OUTPUT: Same thread: True
```

**LOGIC:** By comparing thread IDs, we can verify both the caller and signal handler execute in the same thread. No thread switching occurs.

---

### Question 3: By default, do django signals run in the same database transaction as the caller?

**ANSWER:** Yes

**PROOF CODE:**
```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models, transaction
from django.db import connection

class TestModel(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        app_label = 'assessment_app'

@receiver(post_save, sender=TestModel)
def test_signal_handler(sender, instance, created, **kwargs):
    # Check if we're in a transaction context
    in_atomic = transaction.get_connection().in_atomic_block
    print(f"Signal - In transaction: {in_atomic}")

# Test 1: Autocommit (Django default)
print("Test 1: Autocommit mode")
print(f"Before create - In atomic: {transaction.get_connection().in_atomic_block}")
TestModel.objects.create(name="Test1")
print()

# Test 2: Explicit transaction
print("Test 2: Explicit transaction")
with transaction.atomic():
    print(f"Before create - In atomic: {transaction.get_connection().in_atomic_block}")
    TestModel.objects.create(name="Test2")
    print(f"After signal - In atomic: {transaction.get_connection().in_atomic_block}")

# CONCLUSION: Signal and caller share the same transaction context
```

**LOGIC:** The signal handler executes within the same transaction context as the caller. In autocommit mode, each is its own transaction. In explicit atomic blocks, the signal handler is included in that block.

---

## TOPIC 2: CUSTOM CLASSES IN PYTHON

### Description: Rectangle Class with Iterator Support

You are tasked with creating a Rectangle class with the following requirements:
1. An instance requires `length:int` and `width:int` to be initialized
2. We can iterate over a Rectangle instance
3. When iterated, yield `{'length': <VALUE_OF_LENGTH>}` first, followed by `{'width': <VALUE_OF_WIDTH>}`

**ANSWER:**

```python
class Rectangle:
    """
    A Rectangle class that supports iteration.
    
    Requirements met:
    1. Requires length and width (both integers) in constructor
    2. Is iterable via __iter__ implementation
    3. When iterated, yields length first, then width in specified format
    """
    
    def __init__(self, length: int, width: int):
        """Initialize Rectangle with length and width."""
        self.length = length
        self.width = width
    
    def __iter__(self):
        """
        Make Rectangle iterable.
        Yields {'length': VALUE} then {'width': VALUE}
        """
        yield {'length': self.length}
        yield {'width': self.width}
    
    def __repr__(self):
        """String representation for debugging."""
        return f"Rectangle(length={self.length}, width={self.width})"


# USAGE EXAMPLE:
if __name__ == "__main__":
    rect = Rectangle(length=10, width=5)
    
    # Verify instance creation
    print(f"Rectangle: {rect}")
    
    # Verify iteration output
    print("Iterating over rectangle:")
    for dimension in rect:
        print(dimension)
    
    # Expected Output:
    # {'length': 10}
    # {'width': 5}
```

**LOGIC:** 
- The `__init__` method stores length and width as instance attributes
- The `__iter__` method uses `yield` to make the class iterable
- First iteration yields `{'length': self.length}`
- Second iteration yields `{'width': self.width}`
- The `__repr__` method provides a developer-friendly representation

---

## SUBMISSION CHECKLIST

✅ Django Signals - Question 1: Synchronous execution proven with timing
✅ Django Signals - Question 2: Same thread proven with thread ID comparison
✅ Django Signals - Question 3: Same transaction proven with transaction context
✅ Rectangle Class: Implements all required features
✅ Code is clear, focused on logic over elegance
✅ All code snippets are executable and testable
✅ No external dependencies beyond Django and Python stdlib
