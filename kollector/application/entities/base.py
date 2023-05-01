"""
Base Entity
"""
from pydantic import BaseModel


class BaseEntityModel(BaseModel):
    """
    Base Entity Model
    """

    id: str
    created_at: str = None
    updated_at: str = None
    is_deleted: bool = False
    deleted_at: str = None

    class Config:
        orm_mode = True
