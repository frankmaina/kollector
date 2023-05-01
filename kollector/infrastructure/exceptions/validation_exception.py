from typing import Any, Dict, Optional

from fastapi import HTTPException


class ValidationException(HTTPException):
    """
    Exception raised when a validation error occurs.
    """

    def __init__(
        self,
        detail: Any = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> None:
        status_code = 400
        super().__init__(status_code=status_code, detail=detail, headers=headers)
