from fastapi import APIRouter
from fake import creature as service
from model.creature import Creature

router = APIRouter(prefix='/creature', tags=['Creature'])


@router.get('/')
def get_all() -> list[Creature]:
    return service.get_all()


@router.get('/{name}')
def get_one(name: str) -> Creature | None:
    return service.get_one(name)


@router.post('/')
def create(explorer: Creature) -> Creature:
    return service.create(explorer)


@router.put('/')
def replace(explorer: Creature) -> Creature:
    return service.replace(explorer)


@router.patch('/')
def modify(explorer: Creature) -> Creature:
    return service.modify(explorer)


@router.delete('/{name}')
def delete(name: str):
    return service.delete(name)
