from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse


class CustomError(Exception):
    """Base class for all custom exceptions"""


class CreateEntityError(CustomError):
    def __init__(self, message: str = "Failed to create entity.", *args):
        super().__init__(message, *args)

    def __str__(self) -> str:
        return self.args[0]


class CreateLocationCategoryReviewedError(CustomError):
    def __init__(
        self,
        message: str = "Failed to create location category reviewed.",
        *args,
    ):
        super().__init__(message, *args)

    def __str__(self) -> str:
        return self.args[0]


async def handle_custom_error_422(
    request: Request, exc: CustomError
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"message": str(exc)},
    )


async def handle_custom_error_404(
    request: Request, exc: CustomError
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": str(exc)},
    )


def exception_container(app: FastAPI) -> None:
    app.exception_handler(CreateEntityError)(handle_custom_error_422)
    app.exception_handler(CreateLocationCategoryReviewedError)(
        handle_custom_error_404
    )
