
from django.core.mail.message import EmailMessage


def email_send(subject,message,to_email):
    email = EmailMessage(
        subject,message,to=[to_email]
    )
    email.send()
    return 0