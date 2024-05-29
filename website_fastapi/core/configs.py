import os
from functools import lru_cache
from pydantic_settings import BaseSettings 
from sqlalchemy.orm import declarative_base

script_dir = os.path.dirname(__file__)


template_dir = os.path.join(script_dir, "templates/")


class Settings(BaseSettings):
    DB_URL: str = 'postgresql+asyncpg://postgres:'
    # TEMPLATES:any = Jinja2Templates(directory='templates/')
    #MEDIA: any = Path('media')



@lru_cache()
def get_settings() -> Settings:
    return Settings()
