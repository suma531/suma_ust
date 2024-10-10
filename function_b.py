def function_b():
    with open('inputs/input.txt', 'r') as file:
        data = file.read()
    return f"Function B received: {data.strip()}"

