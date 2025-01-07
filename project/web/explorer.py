from fastapi import APIRouter
from fastapi.params import Depends

from model.explorer import Explorer
import fake.explorer as service
from model.tools import Pagination, Ordering, paginate, sort

router = APIRouter(prefix='/explorer', tags=['Explorer'])


@router.get('/')
def get_all(data: list[Explorer] = Depends(service.get_all)) -> list[Explorer]:
    return data


@router.get('/{name}')
def get_one(name: str) -> Explorer | None:
    return service.get_one(name)


@router.post('/')
def create(explorer: Explorer) -> Explorer:
    return service.create(explorer)


@router.put('/')
def replace(explorer: Explorer) -> Explorer:
    return service.replace(explorer)


@router.patch('/')
def modify(explorer: Explorer) -> Explorer:
    return service.modify(explorer)


@router.delete('/{name}')
def delete(name: str):
    return service.delete(name)
