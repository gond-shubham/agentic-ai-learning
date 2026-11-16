import httpx

data = {"title": "Learning Agentic AI"}

response= httpx.patch("https://jsonplaceholder.typicode.com/posts/1", json= data)

print(response.status_code)
print(response.request.headers)
print(response.json())
print(response.text)