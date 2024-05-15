import time
import asyncio


# Пример использования синхронного контекстного менеджера
# Класс контекстного менеджера
class Timer:
    def __enter__(self):
        self.start_time = time.time()
        print(f"Timer started at {self.start_time}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        stoped_time = time.time()
        elapsed_time = stoped_time - self.start_time
        print(f"Timer stopped at {stoped_time}")
        print(f"Elapsed time: {elapsed_time} seconds")


with Timer() as timer:
    # Ваш блок кода
    # time.sleep(1)
    ...


# Пример использования асинхронного контекстного менеджера
class AsyncTimer:
    def __enter__(self):
        self.start_time = asyncio.get_event_loop().time()
        print(f"Timer started at {self.start_time}")
        return self

    def __aexit__(self, exc_type, exc_val, exc_tb):
        stoped_time = asyncio.get_event_loop().time()
        print(f"Timer stopped at {stoped_time}")
        elapsed_time = stoped_time - self.start_time
        print(f"Elapsed time: {elapsed_time} seconds")


async def example():
    async with AsyncTimer() as timer:
        print("Ваш асинхронный блок кода")
        # Ваш асинхронный блок кода
        # timer.sleep(1)
        await asyncio.sleep(2)

# Запуск асинхронной функции
asyncio.run(example())
