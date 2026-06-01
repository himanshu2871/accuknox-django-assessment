# Question 1: Are Django signals executed synchronously or asynchronously by default?

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
    """
    This signal handler will execute SYNCHRONOUSLY and block until complete.
    """
    print(f"Signal handler started at: {time.time()}")
    time.sleep(2)  # Simulate work
    print(f"Signal handler ended at: {time.time()}")

def run_test_q1():
    """Demonstrate that signals are synchronous"""
    start = time.time()
    print(f"Before save: {start}")
    TestModel.objects.create(name="Test")
    end = time.time()
    print(f"After save: {end}")
    print(f"Total time elapsed: {end - start:.2f} seconds")
    print("\nCONCLUSION: If signals were async, this would finish in <0.1s.")
    print("Since it takes ~2 seconds, signals are SYNCHRONOUS.\n")

# ANSWER: **Synchronously**
