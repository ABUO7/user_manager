from ninja import Router
from .schemas import RegisterSchema, LoginSchema, UpdateUserSchema, TokenOut, RefreshIn, RefreshOut
from .services import register_user, login_user, update_user_profile, refresh_access_token
from .dependencies import JWTAuth

router = Router()


@router.post("/register", response={200: dict, 400: dict})
def register(request, data: RegisterSchema):
    user = register_user(data)
    return {"detail": "Пользователь успешно зарегистрирован"}

@router.post("/login", response={200: TokenOut, 401: dict})
def login(request, data: LoginSchema):
    return login_user(data)

@router.get("/me", auth=JWTAuth(), response={200: RegisterSchema})
def me(request):
    return request.user

@router.put("/me/update", auth=JWTAuth(), response={200: dict})
def update_me(request, data: UpdateUserSchema):
    update_user_profile(request.user, data)
    return {"detail": "Профиль обновлён"}


@router.post("/refresh", response={200: RefreshOut, 400: dict})
def refresh(request, data: RefreshIn):
    return refresh_access_token(data.refresh)


