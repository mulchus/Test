# Почему вычислять большие значения в асинхронной функции плохо?
#
# Асинхронность (asyncio) в Python не выполняет код параллельно, а переключается между задачами во время ожидания (I/O-bound).
# Если в async-функции делать тяжёлые вычисления (CPU-bound), это блокирует asyncio, потому что в Python есть GIL (Global Interpreter Lock).
# Асинхронность в Python подходит для ввода-вывода (I/O-bound)
# Асинхронность позволяет выполнять задачи без блокировки, но только если они ждут чего-то (файлы, сеть, БД).

import asyncio
import aiohttp
import multiprocessing
import concurrent.futures


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


# Проблема с `async` и тяжёлыми вычислениями (CPU-bound)
# Если в async-функции делать тяжёлые вычисления, Python не сможет переключаться между задачами.

async def heavy_task(n):
    print(f"Вычисляю {n}...")
    total = sum(i**2 for i in range(n))  # Долгий процесс
    return total


def heavy_computation(n):
    return sum(i**2 for i in range(n))


async def main():

    urls = ["https://example.com"] * 5
    results = await asyncio.gather(*(fetch(url) for url in urls))
    print(results)

    # Проблема с `async` и тяжёлыми вычислениями (CPU - bound)
    # Если в async-функции делать тяжёлые вычисления, Python не сможет переключаться между задачами.
    results = await asyncio.gather(heavy_task(10 ** 7), heavy_task(10 ** 7))
    print(results)


    # Как правильно выполнять вычисления в `async`?
    # Использовать `asyncio.to_thread()` (делегирование в потоки)
    # В Python 3.9+ можно выполнять CPU-задачи в отдельных потоках, не блокируя asyncio.
    result = await asyncio.to_thread(heavy_computation, 10**7)
    print(result)


    # Использовать `multiprocessing` (запуск на нескольких ядрах)
    # Так как Python использует GIL, единственный способ выполнять настоящий параллелизм — это multiprocessing.

    # не зашло: concurrent.futures.process.BrokenProcessPool: A process in the process pool was terminated abruptly
    # while the future was running or pending.
    with concurrent.futures.ProcessPoolExecutor() as ex:
        loop = asyncio.get_running_loop()
        print(loop)
        result = await loop.run_in_executor(ex, heavy_computation, 10 ** 7)
        print(result)


    # не зашло: AttributeError: 'Pool' object has no attribute 'submit'
    loop = asyncio.get_running_loop()
    with multiprocessing.Pool() as pool:
        print(pool)
        result = await loop.run_in_executor(pool, heavy_computation, 10**7)
        print(result)

asyncio.run(main())
