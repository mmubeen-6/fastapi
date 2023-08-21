import psycopg2
from config_service import configs


def setup_database() -> None:
    if not check_db_exists():
        print("Database does not exists!")
        init_db()


def check_db_exists() -> bool:
    """Checks if the database exists in the PostgreSQL server.

    Returns:
        bool: True if the database exists, False otherwise.
    """
    dbname = configs["POSTGRES_DB"]
    exists = False
    conn = None

    try:
        # Connect to the default 'postgres' database
        conn = psycopg2.connect(
            database="postgres",
            user=configs["POSTGRES_USER"],
            password=configs["POSTGRES_PASSWORD"],
            host=configs["POSTGRES_HOST"],
            port=configs["POSTGRES_PORT"],
        )
        conn.autocommit = True
        cur = conn.cursor()

        # Query the pg_database table to check for the existence of the target database
        cur.execute(f"SELECT 1 FROM pg_database WHERE datname='{dbname}';")
        exists = bool(cur.fetchone())
        cur.close()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()
    return exists


def init_db() -> None:
    """Initializes the database if it does not exist.

    Args:
        cursor (psycopg2.extensions.cursor): Cursor object.
        db_name (str): Database name.
    """

    db_name = configs["POSTGRES_DB"]
    conn = None

    try:
        conn = psycopg2.connect(
            database="postgres",
            user=configs["POSTGRES_USER"],
            password=configs["POSTGRES_PASSWORD"],
            host=configs["POSTGRES_HOST"],
            port=configs["POSTGRES_PORT"],
        )
        cur = conn.cursor()
        cur.execute("CREATE DATABASE %s;", (db_name,))
    # except psycopg2.databases.DuplicateDatabase as e:
    #     print(f"Database {dbname} already exists!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            cur.close()


def setup_tables() -> None:
    """Setups the tables in the database if they do not exist."""

    conn = None
    try:
        conn = psycopg2.connect(
            host=configs["POSTGRES_HOST"],
            port=configs["POSTGRES_PORT"],
            database=configs["POSTGRES_DB"],
            user=configs["POSTGRES_USER"],
            password=configs["POSTGRES_PASSWORD"],
        )
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE public.posts
            (
                id serial NOT NULL,
                title character varying NOT NULL,
                content character varying NOT NULL,
                published boolean NOT NULL DEFAULT TRUE,
                created_at timestamp with time zone NOT NULL DEFAULT NOW(),
                PRIMARY KEY (id)
            );
            ALTER TABLE IF EXISTS public.posts
                OWNER to fastapi;
        """
        )
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()
    return
