import threading
import time

def task(name):
    print(f"{name} начал работу")
    time.sleep(2)
    print(f"{name} завершил работу")

# Создаём два потока
t1 = threading.Thread(target=task, args=("Поток 1",))
t2 = threading.Thread(target=task, args=("Поток 2",))

t1.start()
t2.start()

t1.join()
t2.join()
print("Все потоки завершены")
