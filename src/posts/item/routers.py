from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from src.container import Container


router = APIRouter()


@router.get("/item")
def get_items():
    return {'item': "test_item"}
