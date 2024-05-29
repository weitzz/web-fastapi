import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .views import home_view

script_dir = os.path.dirname(__file__)
st_abs_file_path = os.path.join(script_dir, "static/")
media = os.path.join(script_dir, "media/")


app = FastAPI(docs_url=None, redoc_url=None)
app.include_router(home_view.router)
app.mount("/static", StaticFiles(directory=st_abs_file_path), name="static")
app.mount("/media", StaticFiles(directory=media), name="media")
