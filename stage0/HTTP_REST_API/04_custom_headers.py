import httpx

custom_headers = {
    "X-Application": "IT-Ticket-System",
    "X-Developer": "Python",
    "Accept": "Json/Application"
}


response = httpx.get("https://httpbin.org/headers", headers=custom_headers )

print(response.status_code)
print(response.headers)
print()
print(response.json())   # to check the request header 
print(response.is_success)