from api.response._enum_ import ResponseEnum


class Success200(ResponseEnum):
    """ Успешные ответы с кодом 200 OK """
    REGISTERED = ("USER_REGISTERED", "User successfully registered")
    LOGIN_SUCCESS = ("LOGIN_SUCCESS", "Login successful")
    PROFILE_FETCHED = ("PROFILE_FETCHED", "Profile retrieved successfully")
    PROFILE_UPDATED = ("PROFILE_UPDATED", "Profile updated successfully")
    TOKEN_REFRESHED = ("TOKEN_REFRESHED", "Access token refreshed")
    EMAIL_SENT = ("EMAIL_SENT", "Verification email sent successfully")