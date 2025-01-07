from fastapi import Depends

from model.explorer import Explorer
from model.tools import Pagination, Ordering, sort, paginate

_explorers = [
    Explorer(
        name='Claude Hande',
        country='FR',
        description='Scarce during full moons'
    ),
    Explorer(
        name='Noah Weiser',
        country='DE',
        description='Myopic machete man'
    ),
]


def get_all(pagination: Pagination = Depends(), ordering: Ordering = Depends()) -> list[Explorer]:
    queryset = _explorers
    sorted = sort(queryset, ordering)
    paginated = paginate(sorted, pagination)
    return paginated


def get_one(name: str) -> Explorer | None:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return


def create(explorer: Explorer) -> Explorer:
    return explorer


def modify(explorer: Explorer) -> Explorer:
    return explorer


def replace(explorer: Explorer) -> Explorer:
    return explorer


def delete(name: str) -> bool:
    return True
