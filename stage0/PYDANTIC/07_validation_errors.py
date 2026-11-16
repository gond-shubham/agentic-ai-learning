from pydantic import BaseModel, ValidationError, Field
from typing import Literal

class Customer(BaseModel):
    customer_id:int=Field(gt=0)
    name:str



class AITicket(BaseModel):
    ticket_id:int=Field(gt=0)
    description:str=Field(min_length=10)
    priority:Literal["Low", "Medium", "High"]
    customer:Customer

ticket_data = {
    "ticket_id": -101,
    "description": "Server",
    "priority": "Urgent",
    "customer": {
        "customer_id": "ABC",
        "name": "Rahul"
    }
}

try:
   AITicket.model_validate(ticket_data)
except ValidationError as e:
    print(e.json(indent=4))
    
