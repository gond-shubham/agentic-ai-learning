from typing import TypedDict, Literal, TypeAlias

status: TypeAlias = 	Literal["Low", "Medium", "High"]


class Incident(TypedDict):
    incident_id:int
    description:str
    priority:status
    affected_services: list[str]



class IncidentResponse(TypedDict):
    success:bool
    total_incidents:int
    incidents:list[Incident]



def get_incident_response()->IncidentResponse:
    return{
        "success":True,
        "total_incidents":2,
        "incidents":[{
             "incident_id":101,
             "description":"Email issue",
             "priority":"Medium",
             "affected_services":["email, BAUs"]},
             {
             "incident_id":102,
             "description":"Saas issue",
             "priority":"Medium",
             "affected_services":["incidents, BAUs"]}
        ]
        
    }
