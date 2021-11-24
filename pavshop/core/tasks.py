from celery import shared_task
from core.models import Subscribe
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from pavshop import settings
from product.models import Product
from django.db.models import Count
from users.models import User
from django.utils import timezone
from datetime import timedelta

@shared_task
def send_mail_to_subscribers():
    startdate = timezone.now()
    enddate = startdate - timedelta(days=7)
    send_product = Product.objects.filter(created_at__gte=enddate).annotate(num_rev =Count('review')).order_by('-num_rev')[:1]
    subscriber_emails = Subscribe.objects.values_list('mail', flat=True)
    for mail in subscriber_emails:
        body = render_to_string('subscriber_mail.html', context={
            'email': mail,
            'send_product' : send_product,
        })
        msg = EmailMessage(subject='Subscriber mail', body=body,
                           from_email=settings.EMAIL_HOST_USER,
                           to=[mail, ])
        msg.content_subtype = 'html'
        msg.send(fail_silently=True)


@shared_task
def send_last_login_message():
    startdate = timezone.now()
    enddate = startdate - timedelta(days=30)
    users = User.objects.all()
    send_products = Product.objects.filter(created_at__gte=enddate).annotate(num_rev =Count('review')).order_by('-num_rev')[:5]
    for usr in users:
        if usr.last_login < enddate:
            body = render_to_string('last_login.html', context={
                'send_products' : send_products,
            })
            msg = EmailMessage(subject='Last login', body=body,
            from_email=settings.EMAIL_HOST_USER,
            to = [usr,]
            )
            msg.content_subtype = 'html'
            msg.send(fail_silently=True)
    