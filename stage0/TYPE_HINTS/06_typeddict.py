from typing import TypedDict

class APIResponse(TypedDict):
    status_code:int
    message:str
    success:bool
    data: dict[str, object]


def get_api_response() -> APIResponse:
    return{"status_code":200,
           "message": "API responded successfully. 200 ok",
           "success": True,
           "data": {"name": "Nithin",
                    "Id": 111}}