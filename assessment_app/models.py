from django.db import models


class TestModel(models.Model):
    """
    Test model for demonstrating Django signals behavior.
    Used in assessments Q1, Q2, and Q3.
    """
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'assessment_app'
        verbose_name = 'Test Model'
        verbose_name_plural = 'Test Models'

    def __str__(self):
        return f"{self.name} (Created: {self.created_at})"
