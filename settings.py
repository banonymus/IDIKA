from pydantic import BaseSettings

class Settings(BaseSettings):
    KED_CLIENT_ID: str
    KED_CLIENT_SECRET: str
    KED_TOKEN_URL: str
    KED_AMKA_URL: str

    class Config:
        env_file = ".env"

settings = Settings()
