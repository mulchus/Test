import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect(("localhost", 8080))  # Подключаемся к серверу

    client.send("Привет, сервер!".encode())  # Отправляем сообщение
    response = client.recv(1024).decode()  # Получаем ответ от сервера

    print(f"Ответ сервера: {response}")
