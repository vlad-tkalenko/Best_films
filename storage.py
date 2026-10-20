import sqlite3

DB = "data.db"

def connect():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row      # рядки можна читати як словники (default as a tuple)
    return conn

def init():
    """Створює таблицю, якщо її ще немає."""
    with connect() as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS films (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            year INTEGER NOT NULL,
            category TEXT NOT NULL,
            duration TEXT NOT NULL,
            rating INT NOT NULL,
            actors TEXT NOT NULL)""")

def load(category=None):
    """Повертає список словників, за бажанням лише однієї категорії."""
    init()
    with connect() as conn:
        if category is None:
            rows = conn.execute("SELECT * FROM films ORDER BY year DESC").fetchall()
        else:
            rows = conn.execute("SELECT * FROM films WHERE category = ? ORDER BY year DESC",
                                (category,)).fetchall()
    result = []
    for row in rows:
        result.append(dict(row))
    return result

def add(record: dict):
    """Додає запис і повертає його id."""
    init()
    name, year, category, duration, rating, actors = record['name'], record['year'], record['category'], record['duration'], record['rating'], record['actors']
    with connect() as conn:
        cur = conn.execute("INSERT INTO films (name, year, category, duration, rating, actors) VALUES (?, ?, ?, ?, ?, ?)",
                           (name, year, category, str(duration), rating, actors))
        return cur.lastrowid

def delete(item_id):
    """Видаляє запис. Повертає True, якщо такий був."""
    init()
    with connect() as conn:
        cur = conn.execute("DELETE FROM films WHERE id = ?", (item_id,))
        return cur.rowcount > 0