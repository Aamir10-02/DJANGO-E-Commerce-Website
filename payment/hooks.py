# from paypal.standard.models import ST_PP_COMPLETED
# from paypal.standard.ipn.signals import valid_ipn_received
# from django.dispatch import receiver
# from django.conf import settings
# import time
# from .models import Order
# @receiver(valid_ipn_received)

# def paypal_payment_received(sender, **kwargs):
#     # Add time to pause
#     time.sleep(10)

#     # grab the info that paypal sends
#     paypal_obj = sender
#     # Grab the invoices
#     my_Invoice = str(paypal_obj.invoice)

#     # Match the paypal invoices with the order invoice

#     # Look up the order
#     my_Order = Order.objects.get(invoice=my_Invoice)

#     # Record the order was paid
#     my_Order.paid = True

#     # Save the Order

#     my_Order.save()


#     # print(paypal_obj)
#     # print(f'Amount Paid: {paypal_obj.mc_gross}')

import logging
import time
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from .models import Order

# Configure logging
logger = logging.getLogger(__name__)

@receiver(valid_ipn_received)
def paypal_payment_received(sender, **kwargs):
    time.sleep(10)  # Delay to prevent race conditions

    paypal_obj = sender

    # Log the full IPN data to verify it's reaching the server
    logger.info(f"✅ PayPal IPN Received: {paypal_obj.__dict__}")

    # Extract invoice
    my_Invoice = str(paypal_obj.invoice)

    try:
        # Match the PayPal invoice with the order invoice
        my_Order = Order.objects.get(invoice=my_Invoice)
        my_Order.paid = True  # Mark as paid
        my_Order.save()

        logger.info(f"✅ Order {my_Order.id} marked as PAID")
    except Order.DoesNotExist:
        logger.error(f"❌ Order not found for Invoice {my_Invoice}")
