# Answer - They are executed Synchronously

class TestModel(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        app_label = 'assessment_app'

@receiver(post_save, sender=TestModel)
def test_signal_handler(sender, instance, created, **kwargs):
    print(f"Signal handler started at: {time.time()}")
    time.sleep(2)  # Simulate work
    print(f"Signal handler ended at: {time.time()}")

def run_test_q1():
    start = time.time()
    print(f"Before save: {start}")
    TestModel.objects.create(name="Test")
    end = time.time()
    print(f"After save: {end}")
    print(f"Total time {end - start:.2f}")


