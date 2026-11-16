import asyncio
import httpx
import time


#sequential execution 

async def sequential_execution():
    async with httpx.AsyncClient() as client:
        start=time.perf_counter()
        user1= await client.get("https://jsonplaceholder.typicode.com/users/1")
        post1= await client.get("https://jsonplaceholder.typicode.com/posts/1")
        comment1=await client.get("https://jsonplaceholder.typicode.com/comments/1")
        end=time.perf_counter()

    user1.raise_for_status()
    post1.raise_for_status()
    comment1.raise_for_status()
    print(user1.json())
    print(post1.json())
    print(comment1.json())
    print(f'sequential total execution: {end-start}')



async def concurrent_execution():
    async with httpx.AsyncClient() as client:
        start=time.perf_counter()
        response= await asyncio.gather(client.get("https://jsonplaceholder.typicode.com/users/2"),
                                 client.get("https://jsonplaceholder.typicode.com/posts/2"),
                                 client.get("https://jsonplaceholder.typicode.com/comments/2"))
        end=time.perf_counter()
        for res in response:
            res.raise_for_status()
        for res in response:
            print(res.json())
        print(f'concurrent total execution: {end-start}')


async def main():
    await sequential_execution()
    await concurrent_execution()


asyncio.run(main())




        
        


