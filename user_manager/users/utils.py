from django.core.mail import send_mail
from ninja.errors import HttpError
from user_manager.api.response.error.text import Errors500
from user_manager.api.response.success import Success200


def send_verification_email(email: str, code: str):
    subject = 'Подтверждение почты'
    message = f'Ваш код подтверждения: {code}'
    try:
        send_mail(subject, message, None, [email])
        return Success200.EMAIL_SENT.to_dict()
    except Exception as e:
        raise HttpError(500, Errors500.EMAIL_SENDING_FAILED.to_dict())
