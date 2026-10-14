
import sqlite3

connection = sqlite3.connect("shayak.db")

print("\n--- VOLUNTEERS TABLE STRUCTURE ---")

columns = connection.execute(
    "PRAGMA table_info(volunteers)"
).fetchall()

for column in columns:
    print(column)

print("\n--- EMAIL UNIQUENESS CHECK ---")

indexes = connection.execute(
    "PRAGMA index_list(volunteers)"
).fetchall()

for index in indexes:
    print(index)

print("\n--- DUPLICATE EMAILS ---")

duplicates = connection.execute("""
    SELECT email, COUNT(*)
    FROM volunteers
    GROUP BY email
    HAVING COUNT(*) > 1
""").fetchall()

print(duplicates)

connection.close()
