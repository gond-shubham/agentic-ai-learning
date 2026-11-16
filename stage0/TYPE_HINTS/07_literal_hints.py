from typing import Literal

def update_ticket(ticket_id:int,
                  priority: Literal["Low", "Medium", "High"],
                  status: Literal["Open", "In Progress", "Closed"]) ->dict[str, object]:
    return {"ticket_id":ticket_id,
            "priority":priority,
            "status":status}



print(update_ticket(101, "Low", "Open"))