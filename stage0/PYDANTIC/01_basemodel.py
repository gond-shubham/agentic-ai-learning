from pydantic import BaseModel, ValidationError


class AITicket(BaseModel):
        ticket_id:int      # No need to use constructor __init__
        description:str
        priority:str
        status:str

try:
    ticket1=AITicket(ticket_id=101,
                description="server issue", 
                priority="High", 
                status="inprogress")
    print(ticket1.ticket_id)


    ticket2=AITicket(ticket_id="102",
                description="Network issue", 
                priority="High", 
                status="inprogress")
    print(ticket2.ticket_id)

    

    ticket3=AITicket(ticket_id="ABC",
                description="user issue", 
                priority="High", 
                status="inprogress")
    print(ticket3.ticket_id)
   

except ValidationError as e:
    print(e)






