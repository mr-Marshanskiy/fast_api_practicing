from fastapi import APIRouter, HTTPException

from exceptions import Missing, Duplicate
from service import creature as service
from model.creature import Creature

router = APIRouter(prefix='/creature', tags=['Creature'])


@router.get('/')
def get_all() -> list[Creature]:
    return service.get_all()


@router.get('/{name}')
def get_one(name: str) -> Creature | None:
    try:
        return service.get_one(name)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)


@router.post('/')
def create(explorer: Creature) -> Creature:
    try:
        return service.create(explorer)
    except Duplicate as e:
        raise HTTPException(status_code=404, detail=e.msg)


@router.put('/{name}')
def replace(explorer: Creature) -> Creature:
    return service.replace(explorer)


@router.patch('/{name}')
def modify(name: str, explorer: Creature) -> Creature:
    try:
        return service.modify(name, explorer)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)


@router.delete('/{name}')
def delete(name: str):
    try:
        return service.delete(name)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)
