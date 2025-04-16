from ninja import Router
from .schemas import RegisterSchema, LoginSchema
from .services import register_user, login_user
from .models import CustomUser
from .dependencies import JWTAuth
from ninja.errors import HttpError

router = Router(tags=["Auth"])

# @router.post("/verify-email")
# def verify_email(request, email: str, code: str):
#     try:
#         user = CustomUser.objects.get(email=email)
#         if user.verification_code != code:
#             raise HttpError(400, "Неверный код подтверждения")
#         user.is_email_verified = True
#         user.verification_code = None  # Очистим код
#         user.save()
#         return {"detail": "Email успешно подтвержден"}
#     except CustomUser.DoesNotExist:
#         raise HttpError(404, "Пользователь не найден")



@router.get("/me", auth=JWTAuth(), summary="Текущий пользователь")
def get_me(request):
    user = request.auth
    return {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "phone": user.phone,
        "role": user.role,
    }


@router.post("/register")
def register_user(request, data: RegisterSchema):
    """Регистрация нового пользователя"""
    if CustomUser.objects.filter(email=data.email).exists():
        raise HttpError(400, "Пользователь с таким email уже существует")

    user = register_user(data)
    return {"message": "Регистрация прошла успешно", "user_email": user.email}


@router.post("/login", summary="Login user and return JWT")
def login(request, data: LoginSchema):
    tokens = login_user(email=data.email, password=data.password)
    if not tokens:
        raise HttpError(401, "Неверный email или пароль")
    return tokens
