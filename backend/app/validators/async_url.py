from typing import TYPE_CHECKING

from sqlalchemy import make_url
from sqlalchemy.exc import ArgumentError

from core.custom_exceptions import (
    InstanceExpectedError,
    AsyncDialectExpected,
)

if TYPE_CHECKING:
    from sqlalchemy import URL


class AsyncURLValidator:
    def __set_name__(self, owner, name) -> None:
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, obj, obj_type=None) -> "URL":
        if obj is None:
            raise InstanceExpectedError(f"Need to be invoked via instance, got {obj_type.__name__}")
        
        url_value = getattr(obj, self.private_name, None)

        if url_value is None:
            raise AttributeError("Attempt to access url before setting it!")
        return url_value

    def __set__(self, obj, value) -> None:
        try:
            url_value = make_url(value)
            dialect = None
            if "+" not in url_value.drivername:
                dialect = url_value.drivername
            else: 
                dialect = url_value.drivername.split("+")[1]
            
            if "async" not in dialect and not dialect.startswith("aio"):
                raise AsyncDialectExpected(f"Expected async dialect, but got {dialect}")
            setattr(obj, self.private_name, url_value)
        except ArgumentError:
            raise