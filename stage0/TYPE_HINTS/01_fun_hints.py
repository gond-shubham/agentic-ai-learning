def student_result(name: str, roll_no: int, marks: float, is_passed: bool) -> dict:
    return {
        "name": name,
        "roll_no": roll_no,
        "marks": marks,
        "is_passed": is_passed
    }


std_res=student_result("Nithin", 200, 99.9, True)
print(std_res)