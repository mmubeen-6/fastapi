from typing import List

import models
import schemas
from db import get_db
from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException, Response, status

router = APIRouter(
    prefix="/posts"
)


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[schemas.Post]
)
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts


@router.get(
    "/{post_id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.Post,
)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {post_id} not found",
        )
    return post


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post
)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {post_id} not found",
        )

    db.delete(post)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put(
    "/{post_id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.Post,
)
def update_post(
    post_id: int,
    updated_post: schemas.PostCreate,
    db: Session = Depends(get_db),
):
    db_post_query = db.query(models.Post).filter(models.Post.id == post_id)
    db_post = db_post_query.first()

    if not db_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {post_id} not found",
        )

    db_post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    db.refresh(db_post)
    return db_post
