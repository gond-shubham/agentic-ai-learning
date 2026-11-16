from typing import Literal
from pydantic import BaseModel, field_validator, model_validator, Field, ValidationError


class AITicket(BaseModel):
    ticket_id:int=Field(gt=0)
    description:str=Field(min_length=10, max_length=200)
    priority:Literal["Low", "Medium",  "High"] ="Medium"
    status:Literal[	"Open", "In Progress", "Closed"]="Open"
    resolution:str|None=None

    @field_validator("description")
    @classmethod
    def description_validation(cls, value_d):
        if not value_d.strip():
            raise ValueError("Description cannot be empty")
        return value_d

    @model_validator(mode="after")
    def resolution_validation(self):
        if self.status =="Open" and self.resolution:
            raise ValueError("the open ticket should not have a resolution")

        if self.status =="Closed" and ( not self.resolution or not self.resolution.strip()):
            raise ValueError("the closed ticket must contain resolution..")
        return self


try:
    t1=AITicket(ticket_id=101, 
                description="The server issue",
                priority="Medium",
                status="Open")
except ValidationError as e:
    print(e)


try:
    t2=AITicket(ticket_id=102, 
                description="The server issue",
                priority="Medium",
                status="Closed",
                resolution="The server issue is resolved")
except ValidationError as e:
    print(e)



try:
    t3=AITicket(ticket_id=101, 
                description="The server issue",
                priority="Medium",
                status="Closed")

except ValidationError as e:
    print(e)

try:
    t4=AITicket(ticket_id=101, 
                description="The server issue",
                priority="Medium",
                status="Open",
                resolution="The server issue is resolved")
except ValidationError as e:
    print(e)


try:
    t5=AITicket(ticket_id=101, 
                description="                           ",
               )
except ValidationError as e:
    print(e)

