import socket


def main():
    address = "localhost"
    port = 8080

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((address, port))  # Привязываем сервер к адресу и порту

        while True:
            server.listen(1)  # Ожидаем подключения одного клиента
            print("Сервер запущен и ждёт подключения...")

            conn, addr = server.accept()  # Принимаем подключение
            print(f"Подключен клиент: {addr}")

            data = conn.recv(1024).decode()  # Читаем данные от клиента
            print(f"Клиент прислал: {data}")

            conn.send("Привет от сервера!".encode())  # Отправляем ответ клиенту
            conn.close()  # Закрываем соединение

    except OSError as e:
        print(f"Ошибка: {e}")

    finally:
        server.close()  # Закрываем серверный сокет, если он был открыт


if __name__ == "__main__":
    main()
