import httpx

try:
    response=httpx.get("https://this-domain-does-not-exist-12345.com")
    print(response.is_status)
except httpx.ConnectError:
    print("Connection failed. Unable to reach the server.")
