import asyncio
import time


async def produce(future):
    print(f"Производим результат... (корутина {asyncio.current_task().get_name()})")
    await asyncio.sleep(2)  # Симуляция длительной операции
    future.set_result(f"Результат корутины {asyncio.current_task().get_name()} готов")

async def consume(future):
    print(f"Ожидаем результат... (корутина {asyncio.current_task().get_name()})")
    result = await future  # Ожидаем, пока результат не будет установлен
    print(f"Получен результат: {result}")

async def independent_task():
    print(f"Выполняем независимую задачу... {asyncio.current_task().get_name()}")
    await asyncio.sleep(1)  # Симуляция выполнения независимой задачи
    print("Независимая задача завершена.")

async def main():
    # Создаем объект Future
    future = asyncio.Future()

    # Запускаем производящую, потребляющую и независимую задачи
    # producer = asyncio.create_task(produce(future))
    # consumer = asyncio.create_task(consume(future))
    # independent = asyncio.create_task(independent_task())

    # Ожидаем завершения всех задач
    # await asyncio.gather(producer, consumer, independent)

    # вариант без обертываеие корутин в create_task
    # TODO: а в чем разница? В том, что gather ожидает завершения всех задач, а create_task запускает каждую задачу сразу
    await asyncio.gather(produce(future), consume(future), independent_task())

# Запуск основной асинхронной функции
asyncio.run(main())


# Пример разницы между gather и create_task

async def task(name, delay):
    print(f"Задача {name} начинается...")
    await asyncio.sleep(delay)
    print(f"Задача {name} завершена.")
    return name, delay

async def main():
    # Используем create_task
    task1 = asyncio.create_task(task("A", 2))
    task2 = asyncio.create_task(task("B", 1))

    print("Задачи запущены, продолжаем выполнение...")
    # TODO: а как они здесь могут быть уже запущены без await ?
    time.sleep(3)
    # await asyncio.sleep(3)

    # Ожидаем завершения первой задачи
    result = await task1
    print(f"Результат первой задачи: {result}")

    # Ожидаем завершения второй задачи
    result = await task2
    print(f"Результат второй задачи: {result}")

    print("Все задачи завершены.")

# Запуск основной асинхронной функции
asyncio.run(main())


async def main():
    # Используем gather
    results = await asyncio.gather(
        task("A", 4),
        task("B", 1)
    )
    print(f"Результаты задач: {results}")
    print("Все задачи завершены.")

# Запуск основной асинхронной функции
asyncio.run(main())
