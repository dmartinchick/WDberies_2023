import random
from typing import List

import loguru
from fastapi import APIRouter, Depends, Response, status, Form

from src.posts.item.services import ItemServices
from src.exceptions import ItemNotFoundErorr, NotEnoughItemsError
from src.posts.item.schemas import Item as ItemShema, Enemy, BattleInfo, FightResult
from src.posts.utils import Elo


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
        raise NotEnoughItemsError(e)


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
    try:
        item_services.get_item_by_id(item_id=item.id)
    except ItemNotFoundErorr:
        item_services.add_item(item_id=item.id,
                               brand=item.brand,
                               img_url=item.img_url,
                               name=item.name,
                               price=item.price)
        return item


@router.patch("/items_update/{item_id}", response_model=FightResult)
def update_items_point(battle_info: BattleInfo, item_services: ItemServices = Depends()):

    try:
        item_a = item_services.get_item_by_id(battle_info.current_id)
        item_b = item_services.get_item_by_id(battle_info.enemy_id)

        elo = Elo(item_a_points=item_a.point, item_b_points=item_b.point)
        battle_result = elo.calculate(battle_info.result)

        item_a.point = battle_result.get("item_a")
        item_b.point = battle_result.get("item_b")

        item_services.update_item_point(item=item_a)
        item_services.update_item_point(item=item_b)
        update_item_a = item_services.get_item_by_id(item_a.id)
        update_item_b = item_services.get_item_by_id(item_b.id)
        return {"item_a": update_item_a, "item_b": update_item_b}

    except ItemNotFoundErorr:
        raise ItemNotFoundErorr()
