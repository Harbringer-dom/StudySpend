import sqlite3
import os

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, "database.db")
SCHEMA_PATH = os.path.join(BASE_DIR, "schema.sql")


def init_db():
    if not os.path.exists(SCHEMA_PATH):
        print("schema.sql not found")
        return

    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        schema = f.read()

    conn = sqlite3.connect(DB_PATH)
    try:
        conn.executescript(schema)
        conn.commit()
        print(f"Initialized database at {DB_PATH}")
    finally:
        conn.close()


if __name__ == "__main__":
    init_db()
