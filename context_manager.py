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
        print()


with Timer() as timer:
    # Ваш блок кода
    time.sleep(1)


# Еще пример использования синхронного контекстного менеджера с использованием декоратора
from contextlib import contextmanager

@contextmanager
def timer():
    start_time = time.time()
    print(f"Timer started at {start_time}")
    yield start_time
    stoped_time = time.time()
    print(f"Timer stopped at {stoped_time}")
    elapsed_time = stoped_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")
    print()


with timer() as timer:
    print("Ваш синхронный блок кода")
    time.sleep(1.2)


# Пример использования асинхронного контекстного менеджера
class AsyncTimer:
    async def __aenter__(self):
        self.start_time = asyncio.get_event_loop().time()
        print(f"Timer started at {self.start_time}")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        stoped_time = asyncio.get_event_loop().time()
        print(f"Timer stopped at {stoped_time}")
        elapsed_time = stoped_time - self.start_time
        print(f"Elapsed time: {elapsed_time} seconds")
        print()


async def example():
    async with AsyncTimer() as timering:
        print("Ваш асинхронный блок кода")
        await asyncio.sleep(2)

# Запуск асинхронной функции
asyncio.run(example())


# Еще пример использования асинхронного контекстного менеджера
from contextlib import asynccontextmanager

@asynccontextmanager
async def async_timer():
    start_time = asyncio.get_event_loop().time()
    print(f"Timer started at {start_time}")
    yield start_time
    stoped_time = asyncio.get_event_loop().time()
    print(f"Timer stopped at {stoped_time}")
    elapsed_time = stoped_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")
    print()

async def example():
    async with async_timer() as timer:
        print("Ваш асинхронный блок кода")
        await asyncio.sleep(1.5)

asyncio.run(example())
