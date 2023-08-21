import psycopg2
from config_service import configs
from db import setup_database
from models import post

from fastapi import FastAPI

print(f"configs: {configs}")

setup_database()
app = FastAPI()

# conn = psycopg2.connect(
#     host=configs["POSTGRES_HOST"],
#     port=configs["POSTGRES_PORT"],
#     database=configs["POSTGRES_DB"],
#     user=configs["POSTGRES_USER"],
#     password=configs["POSTGRES_PASSWORD"],
# )


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# if __name__ == "__main__":
#     ...
