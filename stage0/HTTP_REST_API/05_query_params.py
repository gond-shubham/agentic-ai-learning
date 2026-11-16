import httpx

url="https://jsonplaceholder.typicode.com/posts"

response=httpx.get(url, headers={"Accept": "json/applications", "Application": "user_posts"}, params={"userId":1}) 

print(response.url)
print(len(response.json()))
# Access the headers that were SENT in the request
print(response.request.headers)
print(response.status_code)

print("**********************************************************************************")
response1=httpx.get(url, params={"userId":1, "id":3})
print(response1.url)
print(len(response1.json()))
