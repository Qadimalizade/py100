# TODO решите задачу
import json

filename = 'input.json'
def task() -> float:
    with open(filename, encoding="utf-8") as file:
        data = json.load(file)
    result = 1
    counts = 0
    for mean in data:
        result = mean['score'] * mean['weight']
        counts += result
    return round(counts,3)



print(task())
