from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    THREADS_AMOUNT: int
    REQUEST_DELAY_LIMIT: int
    LOG_FILE: str
    URL: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
