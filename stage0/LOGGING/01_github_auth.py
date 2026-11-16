import httpx
import os
from dotenv import load_dotenv
import logging
import configuring_logs

logger = logging.getLogger("github_auth")
logger.info("Github auth is running")

#To load the Environment variables from .env in python environment
load_dotenv(override=True)


token=os.environ.get("GITHUB_TOKEN", )

if token is None:
    logger.error("GITHUB token is not loaded successfully")
    raise ValueError("Github token is missing.")



header={"X-GitHub-Api-Version": "2026-03-10", "Authorization": f'Bearer {token}', "Accept": "application/vnd.github+json"}

response=httpx.get("https://api.github.com/user", headers=header)

if response.is_success:
    logger.info("API request completed successfully.")
else:
    logger.error(f'status code:{response.status_code}-> issue occured while requesting the API')

print(response.status_code)
#print(response.request.headers)
#print(response.headers)
#print(response.text)
print(response.is_success)
