from model.creature import Creature

_explorers = [
    Creature(
        name="Yeti",
        aka="Abominable Snowman",
        country="CN",
        area="Himalayas",
        description="Hirsute Himalayan"
    ),
    Creature(
        name="Bigfoot",
        description="Yeti's Cousin Eddie",
        country="US",
        area="*",
        aka="Sasquatch"
    ),
]


def get_all() -> list[Creature]:
    return _explorers


def get_one(name: str) -> Creature | None:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return


def create(explorer: Creature) -> Creature:
    return explorer


def modify(explorer: Creature) -> Creature:
    return explorer


def replace(explorer: Creature) -> Creature:
    return explorer


def delete(name: str) -> bool:
    return True
