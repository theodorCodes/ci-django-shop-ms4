# Call it each time a line item is attached to the order
# Requires override of default method in checkout/apps.py
# Importing post_save and post_delete from django.db.models.signals
# to signal that either an order has been saved or deleted
from django.db.models.signals import post_save, post_delete
# Import receiver to receive above signals
from django.dispatch import receiver
# Import OrderLineItems as signals are initialized by this object
from .models import OrderLineItem



# Using decorator to signal when products have been saved to call update total
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()



# Using decorator to signal when products have been deleted to call update total
@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    # TEST signal by deleting order in admin and see this message in Terminal
    print('delete signal received!')
    instance.order.update_total()