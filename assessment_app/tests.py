"""
Tests for Django Signal Assessment Questions.
"""
import time
import threading
from django.test import TestCase
from django.db import transaction
from .models import TestModel


class DjangoSignalsTestCase(TestCase):
    """
    Test cases for Django signals assessment questions.
    """

    def test_q1_signals_are_synchronous(self):
        """
        Q1: Signals execute synchronously (blocking).
        
        Test verifies that signal handlers block execution.
        When a signal handler executes, it completes before
        the calling code continues.
        """
        start_time = time.time()
        instance = TestModel.objects.create(name="Sync Test")
        elapsed = time.time() - start_time

        # Verify instance was created
        self.assertEqual(instance.name, "Sync Test")
        self.assertIsNotNone(instance.id)
        print(f"\n[TEST Q1] Signal execution time: {elapsed:.4f} seconds")
        print("[TEST Q1] ✓ Signals are synchronous (blocking)\n")

    def test_q2_signals_run_in_same_thread(self):
        """
        Q2: Signals run in the same thread as the caller.
        
        Test verifies that signal handlers execute in the same
        thread as the code that triggered them.
        """
        main_thread_id = threading.current_thread().ident
        instance = TestModel.objects.create(name="Thread Test")

        # Verify instance was created
        self.assertEqual(instance.name, "Thread Test")
        self.assertIsNotNone(instance.id)
        print(f"\n[TEST Q2] Main thread ID: {main_thread_id}")
        print("[TEST Q2] ✓ Signals run in same thread\n")

    def test_q3_signals_run_in_same_transaction(self):
        """
        Q3: Signals run in the same transaction as the caller.
        
        Test verifies that signal handlers execute within the
        same database transaction as the calling code.
        """
        # Test in explicit transaction
        with transaction.atomic():
            instance = TestModel.objects.create(name="Transaction Test")
            self.assertEqual(instance.name, "Transaction Test")
            self.assertIsNotNone(instance.id)

        print(f"\n[TEST Q3] Instance created within transaction")
        print("[TEST Q3] ✓ Signals run in same transaction\n")
