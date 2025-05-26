# scripts/run_queries.py
from lib.db.connection import get_connection

def authors_for_magazine(magazine_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT DISTINCT a.* FROM authors a
        JOIN articles art ON a.id = art.author_id
        WHERE art.magazine_id = ?
    """, (magazine_id,))
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def magazines_with_multiple_authors():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT m.* FROM magazines m
        JOIN articles art ON m.id = art.magazine_id
        GROUP BY m.id
        HAVING COUNT(DISTINCT art.author_id) >= 2
    """)
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def article_count_per_magazine():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT m.name, COUNT(a.id) as article_count FROM magazines m
        LEFT JOIN articles a ON m.id = a.magazine_id
        GROUP BY m.id
    """)
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def most_prolific_author():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.* FROM authors a
        JOIN articles art ON a.id = art.author_id
        GROUP BY a.id
        ORDER BY COUNT(art.id) DESC
        LIMIT 1
    """)
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

if __name__ == "__main__":
    print("Authors for magazine ID 1:", authors_for_magazine(1))
    print("Magazines with multiple authors:", magazines_with_multiple_authors())
    print("Article count per magazine:", article_count_per_magazine())
    print("Most prolific author:", most_prolific_author())