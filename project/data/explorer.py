from sqlite3 import IntegrityError

from data import curs, conn
from exceptions import Missing, Duplicate
from model.explorer import Explorer


explorer_table_name = 'explorer'

curs.execute(
    f"""
    create table if not exists {explorer_table_name}(
    name text primary key,
    description text,
    country text)
    """
)


def row_to_model(row: tuple) -> Explorer:
    return Explorer(
        name=row[0],
        country=row[1],
        description=row[2],
    )


def model_to_dict(explorer: Explorer) -> dict:
    return explorer.dict() if explorer else None


def get_one(name: str) -> Explorer:
    query = f'select * from {explorer_table_name} where name=:name'
    params = {'name': name}
    curs.execute(query, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    raise Missing(msg=f'Explorer {name} not found.')


def get_all() -> list[Explorer]:
    query = f'select * from {explorer_table_name}'
    curs.execute(query)
    rows = list(curs.fetchall())
    return [row_to_model(row) for row in rows]


def create(explorer: Explorer) -> Explorer:
    query = (f"""insert into {explorer_table_name} values
        (:name, :country, :description)""")
    params = model_to_dict(explorer)
    try:
        curs.execute(query, params)
        conn.commit()
    except IntegrityError as e:
        raise Duplicate(msg=f'Explorer {explorer.name} already exists.')
    return get_one(explorer.name)


def modify(name_orig: str, explorer: Explorer) -> Explorer:
    query = (
        f"""
        update {explorer_table_name} set
            name=:name,
            country=:country,
            description=:description,
        where name=:name_orig
        """
    )
    params = model_to_dict(explorer)
    params['name_orig'] = name_orig
    curs.execute(query, params)
    conn.commit()
    return get_one(name=explorer.name)


def replace(explorer: Explorer) -> Explorer:
    return explorer


def delete(name: str) -> bool:
    if not name:
        return False

    query = f'delete from {explorer_table_name} where name = :name'
    params = {'name': name}
    res = curs.execute(query, params)
    if curs.rowcount != 1:
        raise Missing(msg=f'Explorer {name} not found')
    conn.commit()
    return bool(res)
