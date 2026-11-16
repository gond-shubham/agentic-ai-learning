import httpx

try:
    with httpx.Client(timeout=5.0) as client:
          response=client.get("https://jsonplaceholder.typicode.com/users/1")
          response1=client.get("https://jsonplaceholder.typicode.com/comments/1")
          response2=client.get("https://jsonplaceholder.typicode.com/todos/1")

except ConnectError:
    print("Connection failed. Unable to reach the server.")
except TimeoutException:
    print("Request timed out. Server took too long to respond")
else:
    print(response.status_code, response.text, sep="\n")
    print(response1.status_code, response1.text, sep="\n")
    print(response2.status_code, response2.text, sep="\n")



