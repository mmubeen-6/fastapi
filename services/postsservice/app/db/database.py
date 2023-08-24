from config_service import configs
from sqlalchemy import URL, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

url_object = URL.create(
    "postgresql",
    username=configs["POSTGRES_USER"],
    password=configs["POSTGRES_PASSWORD"],
    host=configs["POSTGRES_HOSTNAME"],
    port=configs["POSTGRES_PORT"],
    database=configs["POSTGRES_DB"],
)
engine = create_engine(url_object)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """Get database session.

    Yields:
        sqlalchemy.orm.sessionmaker
    """
    db = session_local()
    try:
        yield db
    finally:
        db.close()
