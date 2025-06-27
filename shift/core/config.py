from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    title: str = "Shift Test API"
    description: str = "API для получения суммы ЗП и даты следующего повышения"
    db_url: str
    secret: str

    class Config:
        env_file = ".env"


setting = Settings()
