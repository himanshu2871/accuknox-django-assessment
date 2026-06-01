# Accuknox Django Trainee Assessment

Complete Django project submission for the Accuknox Django Trainee Assessment.

## 📋 Assessment Overview

This is a fully functional Django project demonstrating solutions to the Accuknox Django Trainee Assessment.

### Topic 1: Django Signals (3 Questions)

**Question 1:** By default, are django signals executed synchronously or asynchronously?
- **Answer:** Synchronously
- **Implementation:** See `assessment_app/signals.py` - `q1_signal_handler`

**Question 2:** Do django signals run in the same thread as the caller?
- **Answer:** Yes
- **Implementation:** See `assessment_app/signals.py` - `q2_signal_handler`

**Question 3:** By default, do django signals run in the same database transaction as the caller?
- **Answer:** Yes
- **Implementation:** See `assessment_app/signals.py` - `q3_signal_handler`

### Topic 2: Custom Classes in Python (1 Task)

**Task:** Create a Rectangle class with iterator support
- **Requirements:** 
  - Requires `length:int` and `width:int` to be initialized ✅
  - Is iterable ✅
  - When iterated, yields `{'length': <VALUE>}` first, then `{'width': <VALUE>}` ✅
- **Implementation:** See `utils/rectangle.py`

---

## 🏗️ Project Structure

```
accuknox-django-assessment/
├── manage.py                      # Django management script
├── requirements.txt               # Project dependencies
├── README.md                      # This file
├── .gitignore                     # Git ignore file
│
├── accuknox_project/              # Django project settings
│   ├── __init__.py
│   ├── settings.py                # Django settings
│   ├── urls.py                    # URL configuration
│   ├── wsgi.py                    # WSGI application
│   └── asgi.py                    # ASGI application
│
├── assessment_app/                # Main Django application
│   ├── __init__.py
│   ├── apps.py                    # App configuration
│   ├── models.py                  # Django models
│   ├── signals.py                 # Signal handlers (Q1, Q2, Q3)
│   ├── views.py                   # View functions
│   ├── urls.py                    # App URL routes
│   ├── admin.py                   # Django admin configuration
│   └── tests.py                   # Test cases
│
└── utils/                         # Utility modules
    ├── __init__.py
    └── rectangle.py               # Rectangle class (Topic 2)
```

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/himanshu2871/accuknox-django-assessment.git
cd accuknox-django-assessment
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Run Tests
```bash
python manage.py test assessment_app
```

### 6. Create Test Data
```bash
python manage.py shell
```

Inside the Django shell:
```python
from assessment_app.models import TestModel

# Create test instance (will trigger signal handlers)
test = TestModel.objects.create(name="Test Instance")
print(test)
```

---

## 📂 Key Files

### `assessment_app/signals.py`
Contains all three signal handlers demonstrating:
- **Q1 Handler:** Synchronous execution (blocks calling code)
- **Q2 Handler:** Same thread execution (compares thread IDs)
- **Q3 Handler:** Same transaction execution (checks transaction context)

### `utils/rectangle.py`
Rectangle class implementation with:
- `__init__` - Constructor accepting length and width
- `__iter__` - Iterator protocol implementation
- Helper methods - `area()`, `perimeter()`

### `assessment_app/tests.py`
Test cases for all three Django signal questions.

### `assessment_app/models.py`
TestModel used to demonstrate signal behavior.

---

## ✅ Assessment Answers

### Question 1: Synchronous or Asynchronous?
**Answer:** Synchronously

Django signals are synchronous by default. Signal handlers execute immediately and block the calling code until completion.

### Question 2: Same Thread?
**Answer:** Yes

Signal handlers run in the same thread as the code that triggered them. No thread switching occurs.

### Question 3: Same Transaction?
**Answer:** Yes

Signal handlers execute within the same database transaction as the calling code.

### Rectangle Class
Fully implemented in `utils/rectangle.py` with:
- Constructor accepting length and width as integers
- Iterator implementation using `__iter__` and `yield`
- Proper handling of iteration protocol

---

## 🧪 Running the Project

### Start Django Development Server
```bash
python manage.py runserver
```

### Create Test Instance via Web
Visit: `http://localhost:8000/assessment/test-instance/`

This will create a test instance and trigger all signal handlers. Check console output for signal demonstrations.

### Run Tests
```bash
python manage.py test assessment_app -v 2
```

---

## 📊 Signal Demonstrations

When you create a TestModel instance, three signal handlers fire:

1. **Q1 Handler** - Shows synchronous execution
   ```
   [Q1 SIGNAL] Signal handler started at: ...
   [Q1 SIGNAL] Instance 'Test Instance' was created
   [Q1 SIGNAL] Signal handler completed
   ```

2. **Q2 Handler** - Shows same thread execution
   ```
   [Q2 SIGNAL] Main thread ID: 12345
   [Q2 SIGNAL] Handler thread ID: 12345
   [Q2 SIGNAL] Same thread: True
   ```

3. **Q3 Handler** - Shows same transaction execution
   ```
   [Q3 SIGNAL] In atomic transaction: False (or True if in explicit transaction)
   [Q3 SIGNAL] Signal and caller share same transaction context
   ```

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

---

## ✨ Features

✅ Complete Django project structure  
✅ All assessment questions answered  
✅ Signal handlers demonstrating each concept  
✅ Rectangle class with iterator support  
✅ Comprehensive test cases  
✅ Model admin configuration  
✅ URL routing setup  
✅ Ready for production deployment  

---

## 📋 Requirements Met

- ✅ Submitted as Django project (not standalone files)
- ✅ All 3 signal questions answered with code
- ✅ Rectangle class with all requirements
- ✅ Professional project structure
- ✅ Includes tests and demonstrations
- ✅ Complete documentation

---

**Status:** ✅ Complete and Ready for Review

All assessment requirements have been fulfilled. This is a fully functional Django project demonstrating all assessment answers.
