from typing import Text


class IChatError(Exception):
    """Root custom exception"""
    def __init__(self, error_message: Text) -> None:
        self._error_message = error_message

    def __str__(self) -> Text:
        return f"{self._error_message}"


class InvalidDomain(IChatError):
    """Raised when the domain is not valid"""
    def __init__(self, error_message: Text) -> None:
        super(InvalidDomain, self).__init__(error_message)