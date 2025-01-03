from datetime import datetime

from fastapi import FastAPI, Body, Header, Response

from models.tags import TagIn, Tag, TagOut
from services import tags

app = FastAPI()


# @app.get("/hi/{who}/")
# def greet(who: str):
#     return f"Hello? {who}?"


# @app.get("/hi/")
# def greet(who: str):
#     return f"Hello? {who}?"
#


# @app.get("/hi/")
# def greet(who: str = Body(embed=True)):
#     return f"Hello? {who}?"
#


@app.get("/hi/")
def greet(user_agent: str = Header(), who: str = Header()):
    return f"Hello? {who}? {user_agent}"


@app.get("/happy", status_code=200)
def happy(res):
    return ":)"


@app.get("/header/{name}/{value}")
def header(name: str, value: str, response: Response):
    response.headers[name] = value
    return "normal body"


@app.post('/tags/', tags=['TEST'])
def create_tag(tag_in: TagIn) -> TagIn:
    tag: Tag = Tag(tag=tag_in.tag, created=datetime.now(), secret='SDFSDFSDF')
    tags.create(tag)
    return tag_in


@app.get('/tags/{tag_str}')
def get_tag(tag_str: str) -> TagOut:
    tag: Tag = tags.get(tag_str)
    return tag



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)
