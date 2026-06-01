# Accuknox Django Trainee Assessment

Complete solutions to the Django Trainee Assessment for Accuknox with code proofs and comprehensive documentation.

## 📋 Assessment Overview

### Topic 1: Django Signals (3 Questions)

**Question 1:** By default, are django signals executed synchronously or asynchronously?
- **Answer:** Synchronously
- **Proof:** `question_1_synchronous.py`

**Question 2:** Do django signals run in the same thread as the caller?
- **Answer:** Yes
- **Proof:** `question_2_same_thread.py`

**Question 3:** By default, do django signals run in the same database transaction as the caller?
- **Answer:** Yes
- **Proof:** `question_3_same_transaction.py`

### Topic 2: Custom Classes in Python (1 Task)

**Task:** Create a Rectangle class with the following requirements:
1. Requires `length:int` and `width:int` to be initialized
2. Is iterable
3. When iterated, yields `{'length': <VALUE>}` first, then `{'width': <VALUE>}`

- **Answer:** `rectangle_class.py`

## 📁 Project Structure

```
.
├── FINAL_ANSWERS.md              # Formatted answers ready for submission
├── INTERVIEW_EXPLANATIONS.md     # Deep explanations for interview prep
├── question_1_synchronous.py     # Q1: Synchronous execution proof
├── question_2_same_thread.py     # Q2: Same thread execution proof
├── question_3_same_transaction.py # Q3: Same transaction proof
├── rectangle_class.py            # Rectangle class implementation
└── README.md                     # This file
```

## ✅ Quick Answers

| Question | Answer |
|----------|--------|
| Q1: Signals sync/async? | **Synchronously** |
| Q2: Signals same thread? | **Yes** |
| Q3: Signals same transaction? | **Yes** |
| Rectangle class | ✅ Complete implementation |

## 🚀 Key Features

- ✅ All answers are correct and verified
- ✅ Each answer includes working code proof
- ✅ Clear, understandable code focused on logic
- ✅ Professional documentation
- ✅ Interview preparation materials included
- ✅ Real-world examples and explanations

## 📚 Documentation

### FINAL_ANSWERS.md
Formatted answers ready for submission with code proofs for each question.

### INTERVIEW_EXPLANATIONS.md
Deep technical explanations of each concept with:
- Why things work the way they do
- Real-world implications
- Common interview questions and answers
- Talking points for interviews
- Quick reference card

## 💻 Code Files

All Python files are executable and demonstrate the concepts clearly:

### question_1_synchronous.py
Demonstrates that Django signals execute synchronously (blocking). Uses time measurements to prove the signal handler blocks execution.

### question_2_same_thread.py
Demonstrates that Django signals run in the same thread as the caller. Uses thread ID comparison to prove they execute in the same thread.

### question_3_same_transaction.py
Demonstrates that Django signals run in the same database transaction as the caller. Checks transaction context to prove they share the same transaction.

### rectangle_class.py
Complete Rectangle class implementation with:
- `__init__` method that accepts length and width
- `__iter__` method that makes it iterable
- Yields {'length': value} then {'width': value}
- Usage examples and test cases

## 🎓 Learning Outcomes

After reviewing this assessment, you will understand:

### Django Signals
- Why signals are synchronous by design
- How signals maintain thread context
- Why signals share the same transaction
- When to use signals vs. Celery
- How signal handlers affect application performance

### Python Classes & Iterables
- How to implement the iterator protocol
- How generator functions work with `yield`
- Memory efficiency of generators
- Python dunder methods and their purposes
- When to use iterables vs. lists

## 📝 Interview Preparation

This repository includes comprehensive interview preparation materials:

1. **Brief Answers** - Quick 30-second responses
2. **Detailed Explanations** - Complete technical understanding
3. **Real-World Context** - Practical implications
4. **Talking Points** - How to discuss concepts confidently
5. **Common Questions** - Anticipated follow-ups with answers

## ✨ What Makes This Special

- **Proven Correct:** Each answer backed by working code
- **Well-Explained:** Deep technical explanations included
- **Interview-Ready:** Prepared talking points and Q&As
- **Professional Quality:** Clean, well-organized code and documentation
- **Comprehensive:** Everything you need in one place

## 🎯 Assessment Completion

All requirements met:
- ✅ 3 Django Signal questions answered with code proofs
- ✅ 1 Rectangle class implementation with all features
- ✅ Code is clear and focused on logic
- ✅ No unnecessary external dependencies
- ✅ Professional documentation included
- ✅ Interview preparation materials included

## 📞 Quick Reference

**For submission:** See `FINAL_ANSWERS.md`
**For interviews:** See `INTERVIEW_EXPLANATIONS.md`
**For implementation details:** See the `.py` files

---

**Status:** ✅ Complete and Ready for Submission

All answers are correct, proven with code, and professionally documented.
