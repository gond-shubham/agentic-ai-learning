import asyncio

async def fetch_products():
    print("Fetching product details...")
    await asyncio.sleep(5)
    print("Product details fetched")
    return{
        "product_id":1001,
        "product_name":"Phone",
        "price":50000
    }


async def main():
    task = asyncio.create_task(fetch_products())
    print("Processing payment...")
    await asyncio.sleep(2)
    print("Payment processing completed")
    result=await task
    print(result)

if __name__=="__main__":
    asyncio.run(main())