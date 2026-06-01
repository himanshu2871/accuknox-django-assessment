from django.apps import AppConfig


class AssessmentAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'assessment_app'
    verbose_name = 'Django Assessment App'

    def ready(self):
        import assessment_app.signals
