
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def send_notification_email(subject, message, recipient_email, html_template=None):
    if html_template:
        message = render_to_string(html_template, {'username': recipient_email})

    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER, 
        [recipient_email],        
        fail_silently=False,
        html_message=message if html_template else None  
    )


def send_user_block_notification(user_email):
    try:
        send_mail(
            'Account Blocked',
            'Dear user, your account has been blocked by the administrator. Please contact support for further assistance.',
            'pgjishnu10@gmail.com', 
            [user_email],
            fail_silently=False,
        )
    except Exception as e:
        print(f"Error sending email: {e}")