from typing import TypeAlias, Literal, TypedDict

AgentStatus :TypeAlias= Literal["Running", "Completed", "Failed"]


class AgentResponse(TypedDict):
    agent_id:int
    status:AgentStatus
    message:str


def get_agent_response() -> AgentResponse:
    return {"agent_id": 101,
            "status": "Running",
            "message": "Updating the status of the inc"}