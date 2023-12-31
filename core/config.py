import os
from dotenv import load_dotenv 
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
print(os.getenv('POSTGRES_DB'))	

class Settings:
    PROJECT_NAME: str = 'PROYECTO-FAST-API'
    PROJECT_VERSION: str = '1.0'
    POSTGRES_DB: str = os.getenv('POSTGRES_DB')
    POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_SERVER: str = os.getenv('POSTGRES_SERVER')
    POSTGRES_PORT: str = os.getenv('POSTGRES_PORT')

    # SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Neyen1995@localhost:5432/fastapi-database"

    DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}'   


settings = Settings()