import httpx

url="https://jsonplaceholder.typicode.com/users/1"


try:
    response=httpx.get(url, timeout=10.0)
except httpx.TimeoutException:
    print("Request timed out. Server took too long to respond.")
except httpx.NetworkError:
    print("Connection failed. Unable to reach the server.")
else:
    print(response.status_code)
    print(response.is_success)
    print(response.text)
