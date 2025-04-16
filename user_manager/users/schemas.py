from ninja import Schema
from pydantic import EmailStr
from typing import Literal

class RegisterSchema(Schema):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    phone: str
    user_type: Literal["designer", "performer"]

class LoginSchema(Schema):
    email: EmailStr
    password: str

class TokenOut(Schema):
    access: str
    refresh: str
    token_type: str

class RefreshIn(Schema):
    refresh: str

class RefreshOut(Schema):
    access: str
    token_type: str

class UpdateUserSchema(Schema):
    first_name: str
    last_name: str
    phone: str
    user_type: Literal["designer", "performer"]
