import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Создаем таблицу, если её нет
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

def print_users(nomer=1):
    users = cursor.execute("SELECT * FROM users").fetchall()
    print(nomer, users)
    return users

if not print_users():
    # Добавляем пользователя
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("Алиса",))
    conn.commit()  # Сохраняем изменения

print_users(2)

name = "Bob'; DROP TABLE users;--"
cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))

print_users(3)

# name = "Bob'); DROP TABLE users;--"
# query = f"INSERT INTO users (name) VALUES ('{name}')"
## INSERT INTO users (name) VALUES ('Bob'); DROP TABLE users;--')

name = "Bob%'; DROP TABLE users;--"
query = f"SELECT * FROM users WHERE name like '%{name}%'"
print(query)

print(cursor.executescript(query).fetchall())
print_users(4)

# если print(cursor.execute(query).fetchall()), то
# Traceback (most recent call last):
#   File ".\Test\parametrize_sqllite.py", line 31, in <module>
#     print(cursor.execute(query).fetchall())
#           ^^^^^^^^^^^^^^^^^^^^^
# sqlite3.ProgrammingError: You can only execute one statement at a time.
