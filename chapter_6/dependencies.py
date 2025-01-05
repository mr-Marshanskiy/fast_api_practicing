from fastapi import FastAPI, Depends, Path, HTTPException

app = FastAPI()


def user_dep(name: str = Path, password: str = Path):
    return {
        'name': name,
        'valid': True
    }


def check_dep(name: str = Path, password: str = Path):
    if name:
        raise HTTPException(
            status_code=401, detail='Name should be empty',
        )


@app.get('/user')
def get_user(user: dict = Depends(user_dep)) -> dict:
    return user


@app.get('/check_user', dependencies=[Depends(check_dep)])
def check_user() -> bool:
    return True

