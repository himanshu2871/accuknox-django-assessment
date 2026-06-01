from django.urls import path
from . import views

app_name = 'assessment_app'

urlpatterns = [
    path('test-instance/', views.create_test_instance, name='create_test_instance'),
]
