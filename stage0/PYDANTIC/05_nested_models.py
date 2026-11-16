from typing import Literal
from pydantic import BaseModel, Field

class Customer(BaseModel):
    customer_id: int
    name:str
    email:str


class Assignment(BaseModel):
    team:str
    assigned_to:str

class Comment(BaseModel):
    author:str
    message:str


class AITicket(BaseModel):
    ticket_id:int
    description:str
    priority:Literal["Low", "Medium", "High"]
    customer:Customer
    assignment:Assignment
    comments:list[Comment]=[]


t1=AITicket(ticket_id=101,
            description="Migration issue in Production servers",
            priority="High",
            customer={"customer_id":10001,
                      "name":"Nithin Reddy Kommera",
                      "email":"kommerareddy@gmail.com"},
            assignment={"team":"support team",
                        "assigned_to":"Ramesh"},

            comments=[{"author":"Nagesh",
                       "message":"the server migration is started...."},
                       {"author":"Vijesh",
                        "message":"the server migration is completed...."}])

            

print(type(t1.customer))
print(type(t1.assignment))
print(type(t1.comments[0]))


#serialization and deserialization
t1_dict=t1.model_dump()
t1_json=t1.model_dump_json(indent=2)
print(t1_dict)
print(t1_json)


print(type(AITicket.model_validate(t1_dict)))
print(type(AITicket.model_validate_json(t1_json)))