from fastapi import FastAPI

from src.config import logger

from .container import Container
from src.posts.item.routers import router


def create_app(title: str):

    container = Container()
    # db = container.db()

    application = FastAPI(title=title)
    application.container = container
    application.include_router(router)
    return application


app = create_app(title="WDberies")
