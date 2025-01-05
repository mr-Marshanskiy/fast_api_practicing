from fastapi import FastAPI, Depends, Path


def depfunc1(test_param: str = Path):
    pass


def depfunc2(test_param: str = Path):
    pass


app = FastAPI(dependencies=[Depends(depfunc1), Depends(depfunc2)])


@app.get("/main")
def get_main():
    pass

