import os

import dotenv
from fastapi import FastAPI

from web import explorer, creature, user


dotenv.load_dotenv()

app = FastAPI()

app.include_router(explorer.router)
app.include_router(creature.router)
# app.include_router(user.router)


@app.get('/')
def top():
    return 'top here'


@app.get('/echo/{thing}')
def echo(thing):
    return f'echoing {thing}'


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True, port=8002)
