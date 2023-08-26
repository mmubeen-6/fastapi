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


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies a password against its hashed version

    Args:
        plain_password (str): Plaintext password to verify
        hashed_password (str): Hashed password to verify against

    Returns:
        bool: Whether the password is correct
    """
    return pwd_context.verify(plain_password, hashed_password)
