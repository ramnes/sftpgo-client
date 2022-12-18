from enum import Enum


class EventActionHTTPConfigMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"

    def __str__(self) -> str:
        return str(self.value)
