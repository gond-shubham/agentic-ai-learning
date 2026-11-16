import httpx

response = httpx.get(
    "https://jsonplaceholder.typicode.com/users/9999"
)

print(response.status_code)
print(response.is_success)
print(response.json())
response.raise_for_status()