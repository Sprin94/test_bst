from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from robots.models import Robot
from orders.models import Order

TEXT = """
Добрый день!
Недавно вы интересовались нашим роботом модели {model}, версии {version}.
Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами
"""


# TODO лучше вынести в celery
@receiver(post_save, sender=Robot)
def my_handler(sender, created, instance, **kwargs):
    if created:
        orders = (
            Order.objects.select_related("customer").filter(robot_serial=instance.serial)
        )
        for order in orders:
            send_mail(
                subject="Роботы доступны.",
                message=TEXT.format(model=instance.model, version=instance.version),
                from_email=None,
                recipient_list=[order.customer.email],
            )
