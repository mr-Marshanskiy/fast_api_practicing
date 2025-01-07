from fastapi.params import Query
from pydantic import BaseModel


class Pagination(BaseModel):
    offset: int | None = Query(None)
    size: int | None = Query(None)


class Ordering(BaseModel):
    sort: str | None = Query(None)


def paginate(queryset: list[BaseModel], pagination: Pagination):
    return queryset


def sort(queryset: list[BaseModel], ordering: Ordering):
    return queryset
