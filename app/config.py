import os
from datetime import timedelta

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def _get_bool(value, default=False):
    if value is None:
        return default
    return str(value).strip().lower() in {"1", "true", "yes", "on"}


class Config:
    """Configurações da aplicação TrocaTroca."""

    ENVIRONMENT = os.environ.get("APP_ENV", "development").lower()
    DEBUG = _get_bool(os.environ.get("DEBUG"), ENVIRONMENT == "development")

    SECRET_KEY = os.environ.get("SECRET_KEY")
    if not SECRET_KEY and ENVIRONMENT == "production":
        raise RuntimeError("SECRET_KEY deve ser definida no ambiente de produção.")
    if not SECRET_KEY:
        SECRET_KEY = "troca-troca-chave-super-secreta-dev"

    # Banco de dados SQLite local (arquivo trocatroca.db na raiz do backend)
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", f"sqlite:///{os.path.join(BASE_DIR, 'trocatroca.db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Tempo de validade do token de autenticação
    JWT_EXPIRATION = timedelta(hours=24)

    JSON_SORT_KEYS = False
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = ENVIRONMENT == "production"
    SESSION_COOKIE_SAMESITE = "Lax"

    CORS_ALLOWED_ORIGINS = os.environ.get("CORS_ALLOWED_ORIGINS", "*")
