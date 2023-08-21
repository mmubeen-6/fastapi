from typing import Optional

from pydantic import BaseModel


class post(BaseModel):
    title: str
    content: str
    published: Optional[bool] = False
