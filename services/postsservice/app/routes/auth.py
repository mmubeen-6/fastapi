import models
import schemas
from db import get_db
from fastapi.security import OAuth2PasswordRequestForm
from oauth2 import create_access_token
from sqlalchemy.orm import Session
from utils import verify_password

from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter(tags=["Login"])


@router.post("/login", response_model=schemas.Token)
def authenticate_user(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user_db = db.query(models.User).filter_by(email=user_credentials.username).first()
    if user_db is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Credentials"
        )

    if not verify_password(
        plain_password=user_credentials.password, hashed_password=user_db.password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Credentials"
        )

    token = create_access_token(data={"username": user_db.email})

    return schemas.Token(access_token=token, token_type="bearer")
