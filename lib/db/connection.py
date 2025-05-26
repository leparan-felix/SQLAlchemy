import sqlite3
import os

def get_connection():
    conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), '../../articles.db'))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn