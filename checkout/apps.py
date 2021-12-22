from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'


    def ready(self):
        """
        Overriding the ready method and importing our signals module
        """
        import checkout.signals
