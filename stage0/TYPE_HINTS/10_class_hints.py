from typing import TypeAlias, Literal

ticket_priority : TypeAlias=Literal["Low", "Medium", "High"]
ticket_status: TypeAlias = Literal["Open", "In Progress", "Closed"]


class AITicket:
    ticket_count:int=0
    def __init__(self, ticket_id:int,
                 description:str,
                 priority:ticket_priority ,
                 status: ticket_status) -> None:
        self.ticket_id=ticket_id
        self.description=description
        self.priority=priority
        self.status=status
        AITicket.ticket_count+=1

    def update_status(self, new_status:ticket_status) -> None:
        self.status=new_status


    def get_ticket_details(self) -> dict[str, object]:
        return {
            "ticket_id": self.ticket_id,
            "description": self.description,
            "priority": self.priority,
            "status": self.status
        }

    @staticmethod
    def validate_ticket_id(ticket_id: int) -> bool:
        if ticket_id >0:
            return True
        else:
            return False