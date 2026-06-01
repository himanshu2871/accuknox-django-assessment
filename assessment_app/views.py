from django.shortcuts import render
from django.http import JsonResponse
from .models import TestModel


def create_test_instance(request):
    """
    View to create a test instance and trigger signals.
    Visit /assessment/test-instance/ to trigger signal demonstrations.
    """
    instance = TestModel.objects.create(name=f"Test Instance {TestModel.objects.count() + 1}")
    return JsonResponse({
        'message': 'Test instance created',
        'instance_id': instance.id,
        'instance_name': instance.name,
        'note': 'Check console output to see signal demonstrations'
    })
