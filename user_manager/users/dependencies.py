from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from ninja.errors import HttpError
from ninja.security import HttpBearer
from rest_framework_simplejwt.authentication import JWTAuthentication

from ..api.response.error.text import Errors401

User = get_user_model()


class JWTAuth(HttpBearer):
    def authenticate(self, request, token):
        try:
            validated = JWTAuthentication().authenticate(request)
            if not validated:
                raise HttpError(401, Errors401.INVALID_TOKEN.to_dict()
                                )

            user, _ = validated
            if not user or not user.is_active:
                raise HttpError(401, Errors401.USER_INACTIVE.to_dict())

            request.user = user
            return user

        except ObjectDoesNotExist:
            raise HttpError(401, Errors401.USER_NOT_FOUND.to_dict())
        except Exception as e:
            raise HttpError(401, Errors401.UNAUTHORIZED.to_dict())
