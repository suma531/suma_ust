def function_a():
    with open('inputs/input.txt', 'r') as file:
        data = file.read()
    return f"Function A says: {data.strip()}"

