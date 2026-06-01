"""
Django Signals for Assessment.

Demonstrates:
- Q1: Signals are synchronous
- Q2: Signals run in same thread
- Q3: Signals run in same transaction
"""
import time
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from .models import TestModel


# ============================================================================
# QUESTION 1: Are signals synchronous or asynchronous?
# ANSWER: Synchronously
# ============================================================================

@receiver(post_save, sender=TestModel)
def q1_signal_handler(sender, instance, created, **kwargs):
    """
    Q1 Signal Handler - Demonstrates synchronous execution.
    
    When this handler is called, it executes immediately and blocks
    the calling code until completion. If you add a sleep here,
    the save() operation will wait for that sleep to complete.
    """
    if created:
        print(f"[Q1 SIGNAL] Signal handler started at: {time.time()}")
        print(f"[Q1 SIGNAL] Instance '{instance.name}' was created")
        print(f"[Q1 SIGNAL] Signal handler completed")


# ============================================================================
# QUESTION 2: Do signals run in the same thread as the caller?
# ANSWER: Yes
# ============================================================================

main_thread_id = threading.current_thread().ident


@receiver(post_save, sender=TestModel)
def q2_signal_handler(sender, instance, created, **kwargs):
    """
    Q2 Signal Handler - Demonstrates same-thread execution.
    
    This handler runs in the same thread as the code that created
    the TestModel instance. Thread IDs will be identical.
    """
    if created:
        handler_thread_id = threading.current_thread().ident
        print(f"[Q2 SIGNAL] Main thread ID: {main_thread_id}")
        print(f"[Q2 SIGNAL] Handler thread ID: {handler_thread_id}")
        print(f"[Q2 SIGNAL] Same thread: {main_thread_id == handler_thread_id}")


# ============================================================================
# QUESTION 3: Do signals run in the same transaction as the caller?
# ANSWER: Yes
# ============================================================================

@receiver(post_save, sender=TestModel)
def q3_signal_handler(sender, instance, created, **kwargs):
    """
    Q3 Signal Handler - Demonstrates same-transaction execution.
    
    This handler runs within the same database transaction as the
    calling code. If in a transaction.atomic() block, this handler
    is part of that block.
    """
    if created:
        in_atomic = transaction.get_connection().in_atomic_block
        print(f"[Q3 SIGNAL] In atomic transaction: {in_atomic}")
        print(f"[Q3 SIGNAL] Signal and caller share same transaction context")
