from datetime import datetime

from pydantic import BaseModel, EmailStr


class PostBase(BaseModel):
    """Pydantic model representing a post.

    Args:
        BaseModel (pydantic.BaseModel): Pydantic base model.
    """

    title: str
    content: str
    is_published: bool = True


class PostCreate(PostBase):
    """Pydantic model representing a post creation.

    Args:
        PostBase (pydantic Model): Pydantic model representing a post.
    """

    ...


class Post(PostBase):
    id: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    """Pydantic model representing a user.

    Args:
        BaseModel (pydantic.BaseModel): Pydantic base model.
    """

    email: EmailStr
    password: str
