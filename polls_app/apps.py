from django.apps import AppConfig


class PollsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls_app'

    def ready(self):
        import polls_app.auth