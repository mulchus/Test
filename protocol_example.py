from typing import Protocol

class NotificationChannel(Protocol):
    @staticmethod
    def send(user_id: int, message: str) -> None:
        ...

    @staticmethod
    def close() -> None:
        ...

class EmailChannel:  # любой класс автоматически считается соответствующим протоколу, если у него есть нужные методы
    @staticmethod
    def send(user_id: int, message: str) -> None:
        print(f"Send email to user {user_id}: {message}")

    @staticmethod
    def close() -> None:
        print("Close email channel")

class TelegramChannel:  # implement NotificationChannel
    @staticmethod
    def send(user_id: int, message: str) -> None:
        print(f"Send tg message to user {user_id}: {message}")

    @staticmethod
    def close() -> None:
        print("Close TG channel")

class NotificationService:
    def __init__(self, channel: NotificationChannel):
        self.channel = channel

    def send(self, user_id: int, message: str) -> None:
        self.channel.send(user_id, message)

    def close(self) -> None:
        self.channel.close()

email_channel = EmailChannel()
tg_channel = TelegramChannel()
notification_service = NotificationService(email_channel)
notification_service.send(1, "Hello, world!")
notification_service.close()

notification_service = NotificationService(tg_channel)
notification_service.send(1, "Hello, world!")
notification_service.close()

# Send email to user 1: Hello, world!
# Close email channel
# Send tg message to user 1: Hello, world!
# Close TG channel.
