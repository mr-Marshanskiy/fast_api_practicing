import os
from pathlib import Path
from sqlite3 import Connection, connect, Cursor, InternalError


conn: Connection | None = None
curs: Cursor | None = None


def get_db(name: str | None = None, reset: bool = False):
    global conn, curs
    if conn:
        if not reset:
            return
        conn = None

    name = name or os.getenv("CRYPTID_SQLITE_DB")
    if not name:
        top_dir = Path(__file__).resolve().parents[1]
        db_dir = top_dir / 'db'
        db_name = 'cryptid.db'
        db_path = str(db_dir / db_name)
        name = db_path
    conn = connect(name, check_same_thread=False)
    curs = conn.cursor()


get_db()
