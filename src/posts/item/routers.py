import random

import loguru
from fastapi import APIRouter, Depends, Response, status

from src.posts.item.services import ItemServices
from src.exceptions import ItemNotFoundErorr
from src.posts.item.models import Item


router = APIRouter()


@router.get("/items")
def get_all_items(item_services: ItemServices = Depends()):
    return item_services.get_items()


@router.get("/items_is_active")
def get_all_active_items(item_services: ItemServices = Depends()):
    return item_services.get_active_items()


@router.get("/items_random")
def get_random_items(item_services: ItemServices = Depends()):
    items = item_services.get_items_with_img()
    random_items = random.sample(items, 2)
    return random_items


@router.get("/items{item_id}")
def get_item_by_id(item_id: int, item_services: ItemServices = Depends()):
    return item_services.get_item_by_id(item_id)


@router.get("/items_is_not_active")
def get_all_inactive_items(item_services: ItemServices = Depends()):
    return item_services.get_inactive_items()


@router.get("/status")
def get_status():
    return {'status': "Ok"}
