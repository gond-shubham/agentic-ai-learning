from typing import TypeAlias, Literal, TypedDict
status:TypeAlias = 	Literal["Low", "Medium", "High"]

class ticket(TypedDict):
    ticket_id:int
    description:str
    priority:status
    assigned_team:str
    is_urgent:bool

def create_ticket(ticket_id:int, 
                  description:str, 
                  priority:status = "Medium", 
                  assigned_team: str = "Unassigned", 
                  is_urgent:bool=False) -> ticket:
    return{
        "ticket_id":ticket_id,
        "description": description,
        "priority" : priority,
        "assigned_team": assigned_team,
        "is_urgent":is_urgent
    }


def find_ticket(ticket_id:int, assigned_team:str|None=None)-> str|None:
    return assigned_team