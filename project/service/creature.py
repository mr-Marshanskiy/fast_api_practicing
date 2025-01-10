from model.creature import Creature, OptCreature
from data import creature as data


def get_all() -> list[Creature]:
    return data.get_all()


def get_one(name: str) -> OptCreature:
    return data.get_one(name)


def create(creature: Creature) -> OptCreature:
    return data.create(creature)


def modify(name_orig: str, creature: Creature) -> OptCreature:
    return data.modify(name_orig, creature)


def replace(creature: Creature) -> OptCreature:
    return data.replace(creature)


def delete(name: str) -> bool:
    return data.delete(name)
