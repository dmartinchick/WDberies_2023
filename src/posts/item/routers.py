import random

import loguru
from fastapi import APIRouter, Depends, Response, status

from src.posts.item.services import ItemServices
from src.exceptions import ItemNotFoundErorr
from src.posts.item.schemas import Item as ItemShema


router = APIRouter()


@router.get("/items", response_model=list[ItemShema])
def get_all_items(item_services: ItemServices = Depends()):
    return item_services.get_items()


@router.get("/items_is_active", response_model=list[ItemShema])
def get_all_active_items(item_services: ItemServices = Depends()):
    return item_services.get_active_items()


@router.get("/items_random/", response_model=list[ItemShema])
def get_random_items(item_services: ItemServices = Depends()):
    items = item_services.get_items_with_img()
    try:
        random_items = random.sample(items, 2)
        return random_items
    except ValueError as e:
        # loguru.logger.error(e)
        raise ValueError("There are not enough elements in the database to select two random elements" + str(e))
        # TODO: Обработать исключение


@router.get("/items/item_id", response_model=ItemShema)
def get_item_by_id(item_id: int, item_services: ItemServices = Depends()):
    return item_services.get_item_by_id(item_id)


@router.get("/items_is_not_active/", response_model=list[ItemShema])
def get_all_inactive_items(item_services: ItemServices = Depends()):
    return item_services.get_inactive_items()


@router.get("/status")
def get_status():
    return {'status': "Ok"}


@router.post("/items/", response_model=ItemShema)
def create_item(item: ItemShema, item_services: ItemServices = Depends()):
    # TODO: Добавить проверку что фала с таким Id не существует
    item_services.add_item(item_id=item.id,
                           brand=item.brand,
                           img_url=item.img_url,
                           name=item.name,
                           price=item.price)
    return item


@router.post("/items/{items}", response_model=ItemShema)
def update_items_point(item_a: ItemShema, item_b: ItemShema, item_services: ItemServices = Depends()):
    # TODO: реализовать elo
    pass
