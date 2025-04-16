from ninja.security import HttpBearer
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from ninja.errors import HttpError

User = get_user_model()

class JWTAuth(HttpBearer):
    def authenticate(self, request, token):
        try:
            validated = JWTAuthentication().authenticate(request)
            if not validated:
                raise HttpError(401, "Неверный или просроченный токен")

            user, _ = validated
            if not user or not user.is_active:
                raise HttpError(401, "Пользователь неактивен или удален")

            request.user = user
            return user

        except ObjectDoesNotExist:
            raise HttpError(401, "Пользователь не найден")
        except Exception as e:
            raise HttpError(401, f"Аутентификация не удалась: {str(e)}")

