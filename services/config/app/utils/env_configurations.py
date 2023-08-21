import os


def get_env_str(env_variable: str, default: str) -> str:
    return os.getenv(env_variable, default)


def get_env_int(env_variable: str, default: int) -> int:
    try:
        output = int(os.getenv(env_variable, default))
    except ValueError:
        output = default
    return output


def get_env_float(env_variable: str, default: float) -> float:
    try:
        output = float(os.getenv(env_variable, default))
    except ValueError:
        output = default
    return output


def get_env_bool(env_variable: str, default: bool) -> bool:
    try:
        output = os.environ[env_variable].lower() in ["true", "1"]
    except ValueError:
        output = default
    return output
