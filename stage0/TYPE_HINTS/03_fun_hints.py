def signature(
        employee_id:int, 
        employee_name: str, 
        skills:list[str], 
        salary_history:tuple[float,...], 
        department_scores:dict[str, int]) ->set[str]:
    return {"python", "LLMs", "Rest API", "tool calling"}


