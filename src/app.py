from fastapi import FastAPI

from src.config import logger

from src.posts.item.routers import router as item_routers


app = FastAPI(title="WDberies")
app.include_router(item_routers)
