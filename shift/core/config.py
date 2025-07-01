from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    title: str = "Shift Test API"
    description: str = "API для получения суммы ЗП и даты следующего повышения"
    secret: str
    postgres_db: str
    postgres_user: str
    postgres_password: str
    db_host: str
    db_port: int

    class Config:
        env_file = ".env"


setting = Settings()
