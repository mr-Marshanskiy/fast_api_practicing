
import os
from datetime import timedelta

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from exceptions import Missing, Duplicate
from model.user import User
if os.getenv("CRYPTID_UNIT_TEST"):
    from fake import user as service
else:
    from service import user as service


ACCESS_TOKEN_EXPIRE_MINUTES = 30


router = APIRouter(prefix='/user', tags=['User'])


oauth2_dep = OAuth2PasswordBearer(tokenUrl='token')


def unauthorized():
    raise HTTPException(
        status_code=401,
        detail='Incorrect username or password',
        headers={'WWW-Authenticate': 'Bearer'},
    )


@router.post('/token')
async def create_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = service.auth_user(form_data.username, form_data.password)
    if not user:
        unauthorized()
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = service.create_access_token(
        data={'sub': user.username}, expires=expires
    )
    return {'access_token': access_token, 'token_type': 'bearer'}


@router.get('/token')
def get_access_token(token: str = Depends(oauth2_dep)) -> dict:
    return {'token': token}


@router.get('/')
def get_all() -> list[User]:
    return service.get_all()


@router.get('/{name}')
def get_one(name: str) -> User | None:
    try:
        return service.get_one(name)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)


@router.post('/')
def create(user: User) -> User:
    try:
        return service.create(user)
    except Duplicate as e:
        raise HTTPException(status_code=404, detail=e.msg)


@router.put('/')
def replace(user: User) -> User:
    return service.replace(user)


@router.patch('/{name}')
def modify(name: str, user: User) -> User:
    try:
        return service.modify(name, user)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)


@router.delete('/{name}')
def delete(name: str):
    try:
        return service.delete(name)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)
