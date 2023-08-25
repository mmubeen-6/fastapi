from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """Generates a hash from a password

    Args:
        password (str): input password to hash

    Returns:
        str: hashed password
    """
    return pwd_context.hash(password)
