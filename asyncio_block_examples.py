# пример блокировки лупа сихронным кодом

import asyncio
import time

async def bad_task(mode: bool):
    """Запуск задачи ожидания в "плохом" или "хорошем" режиме.
    Args:
        mode (bool): False — плохой режим; True — хороший режим.
    Returns:
        None
    """
    print(f"start test with {mode=}")
    if mode:
        await asyncio.to_thread(time.sleep, 2)
    else:
        time.sleep(2)
    print(f"end test with {mode=}")

async def good_task():
    """Запуск задачи ожидания в асинхронном режиме.
    Returns:
        None
    """
    print("start good")
    await asyncio.to_thread(time.sleep, 2)
    print("end good")

async def main():

    print('\nНеправильный совместный запуск')
    await asyncio.gather(bad_task(False), good_task())
    print('\nПравильный совместный запуск')
    await asyncio.gather(bad_task(True), good_task())

asyncio.run(main())
