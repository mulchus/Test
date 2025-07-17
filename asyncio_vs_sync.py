import requests
from decorators import time_it, async_time_it


REQUEST_COUNT = 10

def fetch(url):
    response = requests.get(url)  # Ждём ответа от сервера
    return response.text

@time_it
def main(urls):
    for num, url in enumerate(urls):
        print(num)
        fetch(url)  # Ждём каждый запрос

main(["https://example.com"] * REQUEST_COUNT)


import asyncio
import aiohttp


async def fetch2(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(response.status)
            return await response.text()

@async_time_it
async def main2(urls):
    tasks = [fetch2(url) for url in urls]
    await asyncio.gather(*tasks)  # Запускаем все запросы одновременно

asyncio.run(main2(["https://example.com"] * REQUEST_COUNT))


# main took 7.979214906692505 seconds to execute.
# main2 took 1.1470463275909424 seconds to execute.
