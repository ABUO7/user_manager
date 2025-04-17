from user_manager.api.response._enum_ import ResponseEnum


class Errors400(ResponseEnum):
    """Ошибки 400 Bad Request"""
    USER_EMAIL_ALREADY_EXISTS = ("USER_EMAIL_ALREADY_EXISTS", "User with this email already exists.")
    USER_PHONE_NUMBER_ALREADY_EXISTS = ("USER_PHONE_NUMBER_ALREADY_EXISTS", "User with this phone number already exists.")
    TOKEN_NOT_VALID = ("TOKEN_NOT_VALID", "Invalid refresh token")
    REFRESH_TOKEN_INVALID = ("REFRESH_TOKEN_INVALID", "Refresh token is invalid or has expired")


class Errors401(ResponseEnum):
    """ Ошибки 401 Unauthorized """
    INVALID_TOKEN = ("INVALID_TOKEN", "Invalid or expired token")
    INVALID_CREDENTIALS = ("INVALID_CREDENTIALS", "Invalid email or password")
    UNAUTHORIZED = ("UNAUTHORIZED", "Authentication failed")
    USER_INACTIVE = ("user_inactive", "User is inactive or has been deleted")
    USER_NOT_FOUND = ("user_not_found", "User not found")


class Errors404(ResponseEnum):
    """Ошибки 404 Not Found"""
    ADMIN_NOT_FOUND = ("ADMIN_NOT_FOUND", "Administration user not found")
    BLOCK_CONFIG_NOT_FOUND = ("BLOCK_CONFIG_NOT_FOUND", "Block configuration not found")
    ALTA_BIO_CLEAN_NOT_FOUND = ("ALTA_BIO_CLEAN_NOT_FOUND", "Alta Bio clean not found")
    ALTA_PRODUCT_NOT_FOUND = ("ALTA_PRODUCT_NOT_FOUND", "Alta product not found")
    CITY_NOT_FOUND = ("CITY_NOT_FOUND", "City not found")
    PUMP_PRESSURE_PIPE_DIAMETER = ("PUMP_PRESSURE_PIPE_DIAMETER_NOT_FOUND", "Pump pressure pipe diameter not found")
    PUMP_PRESSURE_PIPE_COUNT_NOT_FOUND= ("PUMP_PRESSURE_PIPE_COUNT_NOT_FOUND", "Pump pressure pipe count not found")
    ACCEPTED_DIMENSIONS_HEIGHT = ("ACCEPTED_DIMENSIONS_HEIGHT_NOT_FOUND", "Accepted dimensions height not found")
    SUPPLY_MANIFOLD_DIAMETER_NOT_FOUND = ("SUPPLY_MANIFOLD_DIAMETER_NOT_FOUND", "Supply manifold diameter not found")
    INLET_PIPE_NOT_FOUND = ("INLET_PIPE_NOT_FOUND", "Inlet pipe not found")
    PRESSURE_COLLECTOR_DIAMETER_NOT_FOUND = ("PRESSURE_COLLECTOR_DIAMETER_NOT_FOUND", "Pressure collector diameter not found")
    PRESSURE_COLLECTOR_COUNT_NOT_FOUND = ("PRESSURE_COLLECTOR_COUNT_NOT_FOUND", "Pressure collector count not found")
    OUTLET_PIPE_COUNT_NOT_FOUND = ("OUTLET_PIPE_COUNT_NOT_FOUND", "Outlet pipe count not found")
    ACCESSORIES_MATERIAL_NOT_FOUND = ("ACCESSORIES_MATERIAL_NOT_FOUND", "Accessories material not found")
    PIPE_GUIDES_NOT_FOUND  = ("PIPE_GUIDES_NOT_FOUND", "Pipe guides not found")
    CONTROL_CABINET_NOT_FOUND  = ("CONTROL_CABINET_NOT_FOUND", "Control cabinet not found")
    KNS_BUILDING_NOT_FOUND  = ("KNS_BUILDING_NOT_FOUND", "Kns building not found")
    ACCEPTED_DIMENSIONS_DIAMETER_NOT_FOUND  = ("ACCEPTED_DIMENSIONS_DIAMETER_NOT_FOUND", "Accepted dimensions diameter not found")
    PRESSURE_GAUGE_NOT_FOUND = ("PRESSURE_GAUGE_NOT_FOUND", "Pressure gauge not found")


class Errors500(ResponseEnum):
    """Ошибки 500 Internal Server Error"""
    INTERNAL_SERVER_ERROR = ("INTERNAL_SERVER_ERROR", "Error to server, please send message telegram to developer")
    EMAIL_SENDING_FAILED = ("EMAIL_SENDING_FAILED", "Failed to send verification email")

