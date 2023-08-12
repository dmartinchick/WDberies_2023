from fastapi import APIRouter, Depends, Response, status

from src.posts.item.services import ItemService
from src.exceptions import ItemNotFoundErorr


router = APIRouter()


@router.get("/items")
def get_all_items(item_service: ItemService = Depends(ItemService)):
    return item_service.get_items()


@router.get("/status")
def get_status():
    return {'status': "Ok"}
