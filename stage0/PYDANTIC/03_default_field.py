from pydantic import BaseModel, Field
from typing import Literal

class AITicket(BaseModel):
    ticket_id:int
    description:str=Field(min_length=10, max_length=200)
    priority:Literal["Low", "Medium", "High"]="Medium"
    status: Literal["Open", "In Progress", "Closed"]="Open"
    estimated_hours:float|None= Field(default=None, gt=0.0, le=100.0)

ticket1=AITicket(ticket_id=101,description="production server issue")
ticket2=AITicket(ticket_id=102,description="Devlopment server issue", priority="High", status="In Progress",estimated_hours=24.0)



print(ticket2)
print(ticket1)