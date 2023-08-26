from typing import List

import models
from db import engine
from routes import posts, users, auth

from fastapi import FastAPI

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)


@app.get("/")
def test():
    return {"status": "success"}

