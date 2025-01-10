from fastapi import APIRouter, HTTPException
from fastapi.params import Depends

from exceptions import Missing, Duplicate
from model.explorer import Explorer
import service.explorer as service

router = APIRouter(prefix='/explorer', tags=['Explorer'])


@router.get('/')
def get_all(data: list[Explorer] = Depends(service.get_all)) -> list[Explorer]:
    return data


@router.get('/{name}')
def get_one(name: str) -> Explorer | None:
    try:
        return service.get_one(name)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)


@router.post('/')
def create(explorer: Explorer) -> Explorer:
    try:
        return service.create(explorer)
    except Duplicate as e:
        raise HTTPException(status_code=404, detail=e.msg)


@router.put('/')
def replace(explorer: Explorer) -> Explorer:
    return service.replace(explorer)


@router.patch('/{name}')
def modify(name: str, explorer: Explorer) -> Explorer:
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
