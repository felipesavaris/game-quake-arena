from pydantic import BaseModel


class BaseErrorResponse(BaseModel):
    detail: str = 'Internal Server Error'

    def __init__(self, detail: str | None = None) -> None:
        if detail:
            self.detail = detail


class NotFoundErrorResponse(BaseErrorResponse):
    detail: str = 'Not found'


class InternalServerErrorResponse(BaseErrorResponse):
    pass
