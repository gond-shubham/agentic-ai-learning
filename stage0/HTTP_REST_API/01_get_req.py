import httpx
response = httpx.get("https://jsonplaceholder.typicode.com/users/1")


print(response.status_code)
print(response.headers)
print(response.json())
print(response.text)

print(type(response))
print(type(response.json()))
print(response.url)
print(response.is_success)
print(response.raise_for_status())