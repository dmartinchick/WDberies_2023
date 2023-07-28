from fastapi import FastAPI

from .container import Container
from src.posts.item.routers import router


def on_startup():
    container = Container()


app = FastAPI(
    title="WDberies",
    on_startup=on_startup()
)
app.include_router(router)
