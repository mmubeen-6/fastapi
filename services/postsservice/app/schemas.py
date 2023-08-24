from datetime import datetime

from pydantic import BaseModel


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
    created_at: datetime

    class Config:
        orm_mode = True
