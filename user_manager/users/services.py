from django.contrib.auth import authenticate
from django.db import IntegrityError
from ninja.errors import HttpError
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from .models import CustomUser
from .schemas import RegisterSchema, LoginSchema, UpdateUserSchema
from ..api.response.error.text import Errors400, Errors500, Errors401


def register_user(data: RegisterSchema):
    try:
        user = CustomUser.objects.create_user(
            first_name=data.first_name,
            last_name=data.last_name,
            email=data.email,
            password=data.password,
            phone=data.phone,
            user_type=data.user_type,
        )
        return user
    except IntegrityError as e:
        if "unique constraint" in str(e).lower():
            raise HttpError(400, Errors400.USER_EMAIL_ALREADY_EXISTS.to_dict())
        raise HttpError(500, Errors500.INTERNAL_SERVER_ERROR.to_dict())


def login_user(data: LoginSchema):
    user = authenticate(email=data.email, password=data.password)
    if not user:
        raise HttpError(401, Errors401.INVALID_CREDENTIALS.to_dict())
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


def refresh_access_token(refresh_token: str):
    try:
        token = RefreshToken(refresh_token)
        return {
            "access": str(token.access_token),
            "token_type": "Bearer"
        }
    except TokenError:
        raise HttpError(400, Errors400.REFRESH_TOKEN_INVALID.to_dict())
