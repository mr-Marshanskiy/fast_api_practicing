import asyncio

from fastapi import FastAPI


app = FastAPI()


@app.get("/hi/")
async def greet():
    await asyncio.sleep(1)
    return f"Hello? world?"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("greet_async_uvicorn:app", reload=True)
