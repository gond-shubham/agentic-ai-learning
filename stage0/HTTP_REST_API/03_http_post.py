import httpx
url = "https://jsonplaceholder.typicode.com/posts"



post = {
    "userId": 1,
    "title": "Learning HTTPX",
    "body": "Understanding POST requests using Python"
}


response = httpx.post(url, json=post)

print(response.status_code)
print(response.json())
print(response.is_success)

response1=httpx.get("https://jsonplaceholder.typicode.com/posts/10")
print(response.json())