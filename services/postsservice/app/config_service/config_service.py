from utils import get_env_int, get_env_str

configs = {
    "POSTGRES_USER": get_env_str("POSTGRES_USER", "postgres"),
    "POSTGRES_PASSWORD": get_env_str("POSTGRES_PASSWORD", "postgres"),
    "POSTGRES_HOSTNAME": get_env_str("POSTGRES_HOSTNAME", "postgres"),
    "POSTGRES_PORT": get_env_int("POSTGRES_PORT", 5432),
    "POSTGRES_DB": get_env_str("POSTGRES_DB", "postgres"),
    "SECRET_KEY": get_env_str("SECRET_KEY", ""),
}

if not configs["SECRET_KEY"]:
    raise ValueError("No SECRET_KEY set for application")
