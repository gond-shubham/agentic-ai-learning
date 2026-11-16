import asyncio

async def fetch_users():
    print ("Fetching the user details")
    await asyncio.sleep(4)
    print("Successfully fetched user details")
    return {
        "name":"Kommera Nithin reddy",
        "age":24
    }


async def fetch_products():
    print("Fetching the product details")
    await asyncio.sleep(2)
    print("successfully fetched product details")
    return {
        "Product name":"Laptop",
        "product id": 1001,
        "cost":100000
    }

async def fetch_orders():
    print("Fetching order details")
    await asyncio.sleep(3)
    print("Successfully fetched order details")
    return{
        "order id": 101,
        "no of products":2,
        "order cost":120000
    }



async def main():
    result= await asyncio.gather(fetch_users(),
    fetch_products(), fetch_orders())
    print(result)


asyncio.run(main())