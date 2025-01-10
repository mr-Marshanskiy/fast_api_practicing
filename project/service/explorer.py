from model.explorer import Explorer, OptExplorer
from data import explorer as data


def get_all() -> list[Explorer]:
    return data.get_all()


def get_one(name: str) -> OptExplorer:
    return data.get_one(name)


def create(explorer: Explorer) -> OptExplorer:
    return data.create(explorer)


def modify(name_orig: str, explorer: Explorer) -> OptExplorer:
    return data.modify(name_orig, explorer)


def replace(explorer: Explorer) -> OptExplorer:
    return data.replace(explorer)


def delete(name: str) -> bool:
    return data.delete(name)
