# core/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def process_order(order_id):
    # Simulate order processing
    order = Order.objects.get(id=order_id)
    order.status = 'processing'
    order.save()
    return f"Order {order_id} processed successfully"

@shared_task
def send_order_confirmation(order_id):
    order = Order.objects.get(id=order_id)
    send_mail(
        'Order Confirmation',
        f'Your order #{order_id} has been received.',
        'from@example.com',
        [order.user.email],
        fail_silently=False,
    )
    return f"Confirmation email sent for order {order_id}"
