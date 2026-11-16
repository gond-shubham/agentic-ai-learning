def analyse_student(name: str, marks: list[float], subjects:tuple[str,...], student_details:dict[str, str]) -> dict:
    return {
        "name": name,
        "average": sum(marks) / len(marks),
        "subjects": subjects,
        "details": student_details
    }