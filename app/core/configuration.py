"""
    CONFIGURATION FILE
"""
import os
from pathlib import Path
from pydantic import BaseSettings


from dotenv import load_dotenv
load_dotenv()


class Settings(BaseSettings):
    """
    Class to contain the Settings for the application
    """

    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")
    REFRESH_TOKEN_EXPIRE_MINUTES: int = os.environ.get("REFRESH_TOKEN_EXPIRE_MINUTES")
    ALGORITHM = os.environ.get("ALGORITHM")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")  # should be kept secret
    JWT_REFRESH_SECRET_KEY = os.environ.get("JWT_REFRESH_SECRET_KEY")  # should be kept secret

    POSTGRES_HOST: str = os.environ.get("POSTGRES_HOST")
    POSTGRES_USER: str = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD")
    POSTGRES_DB: str = os.environ.get("POSTGRES_DB")
    POSTGRES_PORT: str = os.environ.get("POSTGRES_PORT")
    SCHEME: str = "postgresql"
    SQLALCHEMY_DATABASE_URI = f"{SCHEME}://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

    API_V1_STR = os.environ.get("API_V1_STR")
    PROJECT_NAME = os.environ.get("PROJECT_NAME")

    class Config:
        """
        Config class
        """

        case_sensitive = True


settings = Settings()