import asyncio
import time


#concurrent  execution with gather

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
    await asyncio.gather(fun1(),fun2(),fun3())

start = time.perf_counter()
asyncio.run(main())
end= time.perf_counter()
print(f'concurrent execution time with gather: {end - start}')


    
    