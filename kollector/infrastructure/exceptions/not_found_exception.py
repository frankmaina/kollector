from typing import Any, Dict, Optional
from fastapi import HTTPException


class NotFoundException(HTTPException):
    """
    Exception raised when a resource is not found.
    """

    def __init__(
        self,
        detail: Any = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> None:
        status_code = 404
        super().__init__(status_code=status_code, detail=detail, headers=headers)
