def inspect_data(data: object) -> int|str:
    if isinstance(data, int):
        return data*2
    return f'the input value {data} is not a integer'


print(inspect_data("1"))