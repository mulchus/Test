import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title='ALERT!!!',
            message='Stops Stops Stops Stops Stops !',
            timeout=10
        )
        time.sleep(1)
