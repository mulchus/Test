import aiohttp
import asyncio


async def make_request(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            return html


loop = asyncio.get_event_loop()
some_url = "https://www.example.com"
result_html = loop.run_until_complete(make_request(some_url))
# print(result_html)


# example with cancel task that doesn't finished
async def test():
    print(1)
    await asyncio.sleep(10)
    print(2)


async def main():
    task = asyncio.create_task(test())
    await asyncio.sleep(2)
    task.cancel()

asyncio.run(main())
