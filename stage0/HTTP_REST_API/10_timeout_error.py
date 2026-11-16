import httpx

url="https://httpbin.org/delay/5"


try:
    response=httpx.get(url, timeout=2.0)
except httpx.TimeoutException:
    print("Unable to connect due to timeout")




