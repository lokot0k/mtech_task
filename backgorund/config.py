from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    FILE_NAME: str
    REQUEST_DELAY: int
    URL: str
    DIRECTORY: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
