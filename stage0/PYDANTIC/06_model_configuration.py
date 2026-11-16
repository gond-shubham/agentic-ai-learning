from pydantic import BaseModel, ConfigDict, ValidationError

class AITicket(BaseModel):
    model_config=ConfigDict(extra="forbid", strict=True, validate_assignment=True)
    ticket_id:int
    description:str
    priority:str



try:
    t1=AITicket(ticket_id=101,
                description="Server issue",
                priority="High",
                department="IT")
except ValidationError as e:
    print(e)

try:
    t2=AITicket(ticket_id="101",
                description="Server issue",
                priority="High")
except ValidationError as e:
    print(e)


try:
    t3=AITicket(ticket_id=101,
                description="Server issue",
                priority="High")
except ValidationError as e:
    print(e)


try:
    t3.priority=12345
except ValidationError as e:
    print(e)


