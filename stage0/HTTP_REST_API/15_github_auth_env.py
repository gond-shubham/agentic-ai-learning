import httpx
import os
from dotenv import load_dotenv

#To load the Environment variables from .env in python environment
load_dotenv()

token=os.environ.get("github_token")
print(token is not None)

header={"X-GitHub-Api-Version": "2026-03-10", "Authorization": f'Bearer {token}', "Accept": "application/json"}

response=httpx.get("https://api.github.com/user", headers=header)

print(response.status_code)
print(response.request.headers)
print(response.headers)
print(response.text)
print(response.is_success)
