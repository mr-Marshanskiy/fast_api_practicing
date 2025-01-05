
from fastapi import FastAPI

from creature.data import get_creatures
from creature.models import Creature


app = FastAPI()


@app.get("/creature")
def get_all() -> list[Creature]:
    return get_creatures()
