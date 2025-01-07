from model.creature import Creature
from fake import creature as data


def get_all() -> list[Creature]:
    return data.get_all()


def get_one(name: str) -> Creature | None:
    return data.get_one(name)


def create(explorer: Creature) -> Creature:
    return data.create(explorer)


def modify(explorer: Creature) -> Creature:
    return data.modify(explorer)


def replace(explorer: Creature) -> Creature:
    return data.replace(explorer)


def delete(name: str) -> bool:
    return data.delete(name)
