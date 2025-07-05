from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_payment_confirmation_email(email, booking_reference):
    send_mail(
        subject='Booking Confirmed',
        message=f'Your booking {booking_reference} was successfully paid.',
        from_email='noreply@yourdomain.com',
        recipient_list=[email],
        fail_silently=False,
    )
