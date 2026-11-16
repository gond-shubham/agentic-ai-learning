import asyncio
import time


#concurrent  execution with task
async def fun1():
    print("function 1 operation is started")
    await asyncio.sleep(3)
    print("function 1 operation is completed")

async def fun2():
    print("function 2 operation is started")
    await asyncio.sleep(4)
    print("function 2 operation is completed")

async def fun3():
    print("function 3 operation is started")
    await asyncio.sleep(5)
    print("function 3 operation is completed")




async def main():
    task1=asyncio.create_task(fun1())
    task2=asyncio.create_task(fun2())
    task3=asyncio.create_task(fun3())
    await task1
    await task2
    await task3

start = time.perf_counter()
asyncio.run(main())

end= time.perf_counter()
print(f'concurrent execution time with task: {end - start}')


    
    