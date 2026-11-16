import asyncio
import httpx

async def create_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    data= {
          "userId": 1,
          "title": "going to trip",
          "body": "I am enjoying my goa trip"
          }
    async with httpx.AsyncClient() as client:
          response=await client.post(url, json=data)
          
    response.raise_for_status()
    print(response.json())



asyncio.run(create_post())

