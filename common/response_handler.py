from fastapi import status
from typing import Generic, TypeVar, Union

from pydantic import BaseModel
from fastapi.responses import JSONResponse, Response

T = TypeVar('T')


class APIResponse(BaseModel, Generic[T]):
    success: bool
    msg: str
    code: int
    data: T = None


def success(*, data: T) -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=APIResponse(code=200, msg="success", success=True, data=data).dict()
    )


def success_msg(*, message: str, data: T) -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=APIResponse(code=200, msg=message, success=True, data=data).dict()
    )


def error(*, message: str = "fail") -> Response:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=APIResponse(code=400, msg=message, success=False).dict()
    )


def error_500(*, message: str = "BAD REQUEST", data: str = None) -> Response:
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=APIResponse(code=500, msg=message, success=True, data=data).dict()
    )
