from pydantic import BaseModel
from typing import Literal


class AITicket(BaseModel):
        ticket_id:int      # No need to use constructor __init__
        description:str
        priority: Literal["Low", "Medium", "High"]
        status: Literal["Open", "In Progress", "Closed"]
        assigned_team: str | None
        resolution : str | None


ticket1=AITicket(ticket_id=101,
                description="server issue", 
                priority="High", 
                status="In Progress",
                assigned_team=None,
                resolution=None)


ticket2=AITicket(ticket_id=101,
                description="server issue", 
                priority="High", 
                status="In Progress",
                assigned_team="service desk",
                resolution="pending")


print(ticket1)
print(ticket2)