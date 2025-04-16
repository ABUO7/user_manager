import random
from django.db import IntegrityError
from django.contrib.auth import authenticate
from ninja.errors import HttpError
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from .models import CustomUser
from .schemas import RegisterSchema, LoginSchema, UpdateUserSchema
from .utils import send_verification_email


# def generate_verification_code():
#     return str(random.randint(100000, 999999))

def register_user(data: RegisterSchema):
    try:
        # code = generate_verification_code()
        user = CustomUser.objects.create_user(
            first_name=data.first_name,
            last_name=data.last_name,
            email=data.email,
            password=data.password,
            phone=data.phone,
            user_type=data.user_type,
            # is_active=True,
            # verification_code=code
        )
        # send_verification_email(user.email, code)
        return user
    except IntegrityError as e:
        if "unique constraint" in str(e).lower():
            raise HttpError(400, "Пользователь с таким email уже существует")
        raise HttpError(500, "Ошибка при регистрации")

def login_user(data: LoginSchema):
    user = authenticate(email=data.email, password=data.password)
    if not user:
        raise HttpError(401, "Неверный email или пароль")
    # if not user.is_email_verified:
    #     raise HttpError(403, "Email не подтвержден")
    refresh = RefreshToken.for_user(user)
    return {
        "access": str(refresh.access_token),
        "refresh": str(refresh),
        "token_type": "Bearer"
    }

def update_user_profile(user, data: UpdateUserSchema):
    user.first_name = data.first_name
    user.last_name = data.last_name
    user.phone = data.phone
    user.user_type = data.user_type
    user.save()
    return user

# def logout_user(refresh_token: str):
#     try:
#         token = RefreshToken(refresh_token)
#         token.blacklist()
#         return {"detail": "Вы успешно вышли"}
#     except TokenError:
#         raise HttpError(400, "Невалидный refresh токен")

def refresh_access_token(refresh_token: str):
    try:
        token = RefreshToken(refresh_token)
        return {
            "access": str(token.access_token),
            "token_type": "Bearer"
        }
    except TokenError:
        raise HttpError(400, "Refresh токен невалиден или истёк")
