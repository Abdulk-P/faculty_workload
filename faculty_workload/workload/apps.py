from django.apps import AppConfig


class WorkloadConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'workload'



class WorkloadConfig(AppConfig):
    name = 'workload'

    def ready(self):
        import workload.signals
