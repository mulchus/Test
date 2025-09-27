import multiprocessing
import time

def task(name):
    print(f"{name} начал работу")
    time.sleep(2)
    print(f"{name} завершил работу")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=task, args=("Процесс 1",))
    p2 = multiprocessing.Process(target=task, args=("Процесс 2",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("Все процессы завершены")
