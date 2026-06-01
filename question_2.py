# Answer - Yes they run in the same thread as the caller


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

def run_test_q2():
    TestModel.objects.create(name="Test")
    print("The signal handler ran in the sam thread")
