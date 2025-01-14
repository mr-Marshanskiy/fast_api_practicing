from sqlite3 import IntegrityError

from data import curs, conn
from exceptions import Missing, Duplicate
from model.user import User


table_name = 'user'
x_table_name = 'xuser'

curs.execute(
    f"""
    create table if not exists {table_name}(
    name text primary key,
    hash text)
    """
)
curs.execute(
    f"""
    create table if not exists {x_table_name}(
    name text primary key,
    hash text)
    """
)


def row_to_model(row: tuple) -> User:
    name, hash = row
    return User(
        name=name,
        hash=hash,
    )


def model_to_dict(user: User) -> dict:
    return user.model_dump() if user else None


def get_one(name: str, table: str = table_name) -> User:
    query = f'select * from {table} where name=:name'
    params = {'name': name}
    curs.execute(query, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    raise Missing(msg=f'User {name} not found.')


def get_all(table: str = table_name) -> list[User]:
    query = f'select * from {table}'
    curs.execute(query)
    rows = list(curs.fetchall())
    return [row_to_model(row) for row in rows]


def create(user: User, table: str = table_name) -> User:
    query = (f"""insert into {table} values
        (:name, :hash)""")
    params = model_to_dict(user)
    try:
        curs.execute(query, params)
        conn.commit()
    except IntegrityError as e:
        raise Duplicate(msg=f'User {user.name} already exists.')
    return get_one(user.name, table=table)


def modify(name_orig: str, user: User) -> User:
    query = (
        f"""
        update {table_name} set
            name=:name,
            hash=:hash
        where name=:name_orig
        """
    )
    params = model_to_dict(user)
    params['name_orig'] = name_orig
    curs.execute(query, params)
    conn.commit()
    return get_one(name=user.name)


def replace(user: User) -> User:
    return user


def delete(name: str) -> bool:
    if not name:
        return False

    user = get_one(name)
    query = f'delete from {table_name} where name = :name'
    params = {'name': name}
    res = curs.execute(query, params)
    if curs.rowcount != 1:
        raise Missing(msg=f'User {name} not found')
    conn.commit()
    create(user, table=x_table_name)
    return bool(res)
