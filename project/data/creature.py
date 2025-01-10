from sqlite3 import IntegrityError

from data import curs, conn
from exceptions import Missing, Duplicate
from model.creature import Creature


creature_table_name = 'creature'

curs.execute(
    f"""
    create table if not exists {creature_table_name}(
    name text primary key,
    description text,
    country text,
    area text,
    aka text)
    """
)


def row_to_model(row: tuple) -> Creature:
    name, description, country, area, aka = row
    return Creature(
        name=name,
        description=description,
        country=country,
        area=area,
        aka=aka,
    )


def model_to_dict(creature: Creature) -> dict:
    return creature.model_dump() if creature else None


def get_one(name: str) -> Creature:
    query = f'select * from {creature_table_name} where name=:name'
    params = {'name': name}
    curs.execute(query, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    raise Missing(msg=f'Creature {name} not found.')


def get_all() -> list[Creature]:
    query = f'select * from {creature_table_name}'
    curs.execute(query)
    rows = list(curs.fetchall())
    return [row_to_model(row) for row in rows]


def create(creature: Creature) -> Creature:
    query = (f"""insert into {creature_table_name} values
        (:name, :description, :country, :area, :aka)""")
    params = model_to_dict(creature)
    try:
        curs.execute(query, params)
        conn.commit()
    except IntegrityError as e:
        raise Duplicate(msg=f'Creature {creature.name} already exists.')
    return get_one(creature.name)


def modify(name_orig: str, creature: Creature) -> Creature:
    query = (
        f"""
        update {creature_table_name} set
            country=:country,
            name=:name,
            description=:description,
            area=:area,
            aka=:aka
        where name=:name_orig
        """
    )
    params = model_to_dict(creature)
    params['name_orig'] = name_orig
    _ = curs.execute(query, params)
    conn.commit()
    return get_one(creature.name)


def replace(creature: Creature) -> Creature:
    return creature


def delete(name: str) -> bool:
    if not name:
        return False

    query = f'delete from {creature_table_name} where name = :name'
    params = {'name': name}
    res = curs.execute(query, params)
    if curs.rowcount != 1:
        raise Missing(msg=f'Creature {name} not found')
    conn.commit()
    return bool(res)
