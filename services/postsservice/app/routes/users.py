import models
import schemas
from db import get_db
from sqlalchemy.orm import Session
from utils import hash_password

from fastapi import APIRouter, Depends, HTTPException, Response, status

router = APIRouter(
    prefix="/users"
)


@router.post("/", status_code=status.HTTP_200_OK)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user_db = db.query(models.User).filter_by(email=user.email).first()

    if user_db is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists",
        )

    user.password = hash_password(user.password)
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()

    return {"status": "success"}
