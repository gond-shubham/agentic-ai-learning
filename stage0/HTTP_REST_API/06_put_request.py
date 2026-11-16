import httpx
data={"userId": 1,
       "title": "Learning HTTPX - PUT",
       "body" : "Practising how to update an existing resource using PUT."}
    


response=httpx.put("https://jsonplaceholder.typicode.com/posts/1", headers={"Accept": "json/application", "authorization": "Token"}, 
            json=data)


print(response.request.headers)
print(response.status_code)
print(response.text)

