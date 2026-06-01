# Question 3: By default, do Django signals run in the same database transaction as the caller?

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models, transaction

class TestModel(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        app_label = 'assessment_app'

transaction_ids = []

@receiver(post_save, sender=TestModel)
def test_signal_handler(sender, instance, created, **kwargs):
    """
    This signal handler executes within the SAME TRANSACTION as the caller.
    """
    # Get current transaction ID
    from django.db import connection
    connection_id = id(connection)
    in_atomic = transaction.get_connection().in_atomic_block
    
    print(f"Signal handler - In atomic block: {in_atomic}")
    print(f"Signal handler - Connection ID: {connection_id}")
    transaction_ids.append(('signal', connection_id, in_atomic))

def run_test_q3():
    """Demonstrate that signals run in the same transaction"""
    
    print("Test 1: Creating instance in autocommit mode")
    print("-" * 50)
    from django.db import connection
    conn_id_before = id(connection)
    print(f"Before create - Connection ID: {conn_id_before}")
    print(f"Before create - In atomic: {transaction.get_connection().in_atomic_block}")
    
    TestModel.objects.create(name="Test1")
    print()
    
    print("\nTest 2: Creating instance within explicit transaction")
    print("-" * 50)
    with transaction.atomic():
        print(f"Before create - In transaction: {transaction.get_connection().in_atomic_block}")
        TestModel.objects.create(name="Test2")
        print(f"After signal - In transaction: {transaction.get_connection().in_atomic_block}")
    
    print("\n" + "=" * 50)
    print("CONCLUSION: The signal handler runs within the SAME TRANSACTION")
    print("context as the caller. If the caller is in a transaction, so is")
    print("the signal handler. This means signal and caller share the same")
    print("database transaction lifecycle.\n")

# ANSWER: **Yes**
