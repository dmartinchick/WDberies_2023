from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from src.container import Container
from src.posts.item.services import ItemService
from src.exceptions import ItemNotFoundErorr


router = APIRouter()


@router.get("/items")
@inject
def get_all_items(item_service: ItemService = Depends(Provide[Container.item_service])):
    return item_service.get_items()


@router.get("/status")
def get_status():
    return {'status': "Ok"}
