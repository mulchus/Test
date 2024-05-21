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
print(result_html)
