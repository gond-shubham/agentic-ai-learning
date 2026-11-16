import asyncio
import httpx

async def fetch_users():
    async with httpx.AsyncClient() as client:
            response=await client.get("https://jsonplaceholder.typicode.com/users")

    print(response.raise_for_status())
    users=response.json()
    print(users[0]["name"])
    print(users[0]["email"])
    print(users[0]["address"]["city"])
    



asyncio.run(fetch_users())