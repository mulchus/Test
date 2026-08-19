import asyncio

async def slow():
    try:
        print("работа началась")
        await asyncio.sleep(2)
    except asyncio.CancelledError:
        print("работа прервана")
        # raise

async def main():
    task = asyncio.create_task(slow())
    await asyncio.sleep(0.1)
    try:
        # await asyncio.wait_for(asyncio.shield(task), timeout=1)
        await asyncio.wait_for(task, timeout=1)
    except asyncio.TimeoutError:
        print("время вышло")
    await asyncio.sleep(1)

asyncio.run(main())
