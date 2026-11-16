import asyncio
import time


#sequential execution

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
    await fun1()
    await fun2()
    await fun3()

start = time.perf_counter()
asyncio.run(main())
end= time.perf_counter()

print(f'sequential execution time: {end - start}')


    
    