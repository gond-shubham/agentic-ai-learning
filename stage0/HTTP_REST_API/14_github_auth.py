import httpx
import os

token=os.environ.get("GITHUB_TOKEN")
print(token is not None)

header={"X-GitHub-Api-Version": "2026-03-10", "Authorization": f'Bearer {token}', "Accept": "application/json"}

response=httpx.get("https://api.github.com/users/kommeranithinreddy", headers=header)

print(response.status_code)
print(response.request.headers)
print(response.headers)
print(response.text)
print(response.is_success)