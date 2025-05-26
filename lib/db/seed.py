import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from lib.db.connection import get_connection
from scripts.setup_db import setup_database

def seed_database():
    setup_database()  
    
    conn = get_connection()
    cursor = conn.cursor()

    # Clear existing data
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")

    # Seed authors
    authors = [
        ("Jane Ken",),
        ("John Smith",),
        ("Alice Johnson",)
    ]
    cursor.executemany("INSERT INTO authors (name) VALUES (?)", authors)

    # Seed magazines
    magazines = [
        ("Tech Trends", "Technology"),
        ("Health Weekly", "Health"),
        ("Science Digest", "Science")
    ]
    cursor.executemany("INSERT INTO magazines (name, category) VALUES (?, ?)", magazines)

    # Fetch author IDs
    cursor.execute("SELECT id FROM authors WHERE name = 'Jane Ken'")
    row = cursor.fetchone()
    if row is None:
        raise Exception("Author 'Jane Ken' not found.")
    jane_id = row['id']

    cursor.execute("SELECT id FROM authors WHERE name = 'John Smith'")
    row = cursor.fetchone()
    if row is None:
        raise Exception("Author 'John Smith' not found.")
    john_id = row['id']

    cursor.execute("SELECT id FROM authors WHERE name = 'Alice Johnson'")
    row = cursor.fetchone()
    if row is None:
        raise Exception("Author 'Alice Johnson' not found.")
    alice_id = row['id']

    # Fetch magazine IDs
    cursor.execute("SELECT id FROM magazines WHERE name = 'Tech Trends'")
    row = cursor.fetchone()
    if row is None:
        raise Exception("Magazine 'Tech Trends' not found.")
    tech_id = row['id']

    cursor.execute("SELECT id FROM magazines WHERE name = 'Health Weekly'")
    row = cursor.fetchone()
    if row is None:
        raise Exception("Magazine 'Health Weekly' not found.")
    health_id = row['id']

    # Seed articles
    articles = [
        ("AI Revolution", jane_id, tech_id),
        ("Healthy Eating", john_id, health_id),
        ("Quantum Computing", jane_id, tech_id),
        ("Fitness Tips", alice_id, health_id)
    ]
    cursor.executemany("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", articles)

    conn.commit()
    conn.close()
    print("Database seeded with test data.")

if __name__ == "__main__":
    seed_database()
