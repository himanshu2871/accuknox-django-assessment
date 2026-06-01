# Question 2: Do Django signals run in the same thread as the caller?

import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

class TestModel(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        app_label = 'assessment_app'

# Store main thread ID before signal definition
main_thread_id = threading.current_thread().ident

@receiver(post_save, sender=TestModel)
def test_signal_handler(sender, instance, created, **kwargs):
    """
    This signal handler will execute in the SAME THREAD as the caller.
    """
    handler_thread_id = threading.current_thread().ident
    print(f"Main thread ID: {main_thread_id}")
    print(f"Handler thread ID: {handler_thread_id}")
    print(f"Same thread: {main_thread_id == handler_thread_id}")

def run_test_q2():
    """Demonstrate that signals run in the same thread"""
    print("Creating a TestModel instance...\n")
    TestModel.objects.create(name="Test")
    print("\nCONCLUSION: The signal handler ran in the SAME THREAD as the caller.\n")

# ANSWER: **Yes**
