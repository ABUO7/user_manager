from django.core.mail import send_mail

def send_verification_email(email: str, code: str):
    subject = 'Подтверждение почты'
    message = f'Ваш код подтверждения: {code}'
    send_mail(subject, message, None, [email])
