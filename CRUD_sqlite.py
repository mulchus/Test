import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Создаем таблицу, если её нет
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
# Добавляем пользователя
cursor.execute("INSERT INTO users (name) VALUES (?)", ("Алиса",))
conn.commit()  # Сохраняем изменения

n = 1
def print_users():
    global n
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()  # Получаем все записи
    print(n)
    for user in users:
        print(user)
    n += 1

print_users()

# Изменение существующей записи.
cursor.execute("UPDATE users SET name = ? WHERE id = ?", ("Боб", 1))
conn.commit()
print_users()

# Удаление записи из базы.
cursor.execute("DELETE FROM users WHERE id = ?", (1,))
conn.commit()
print_users()


conn.close()
