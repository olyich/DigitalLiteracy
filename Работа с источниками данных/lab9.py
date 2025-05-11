import json


def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)

    total = 0.0
    for item in data:
        score = item["score"]
        weight = item["weight"]
        total += score * weight

    return round(total, 3)


print(task())