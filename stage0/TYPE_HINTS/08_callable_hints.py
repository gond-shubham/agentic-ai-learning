from typing import Callable

def multiply(a:int, b:int) -> int:
    return a*b


def execute_operation(operation: Callable[[int, int], int], x:int, y:int) -> int:
    return operation(x,y)

print(execute_operation(multiply, 10, 10))
           