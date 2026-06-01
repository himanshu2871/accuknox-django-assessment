from django.urls import path, include

urlpatterns = [
    path('assessment/', include('assessment_app.urls')),
]
