import httpx
import asyncio

async def fetch_users():
    url="https://jsonplaceholder.typicode.com/users"
    try:
        async with httpx.AsyncClient() as client:
            response=await client.get(url, timeout=3)
            response.raise_for_status()
    except httpx.HTTPStatusError as h:
        print(h)
    except httpx.TimeoutException as t:
        print(t)
    except httpx.ConnectError as c:
        print(c)
    except httpx.RequestError as r:
        print(r)


asyncio.run(fetch_users())

        

