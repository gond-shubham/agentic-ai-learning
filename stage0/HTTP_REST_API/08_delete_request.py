import httpx

response=httpx.delete(url="https://jsonplaceholder.typicode.com/posts/1")


print(response.status_code)
print(response.request.headers)
print(response.text)