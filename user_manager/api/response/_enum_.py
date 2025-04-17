from enum import Enum


class ResponseEnum(Enum):
    """ Базовый класс для удобных ошибок. """

    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message

    def to_dict(self):
        """ Преобразует ошибку в словарь. """
        return {"code": self.code, "message": self.message}

    def __str__(self):
        return self.message
