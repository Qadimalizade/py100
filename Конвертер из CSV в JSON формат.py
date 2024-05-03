# TODO импортировать необходимые молули
import os
import csv
import json
import pickle

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"




def task() -> None:

    with open(INPUT_FILENAME) as file:
        reader = csv.DictReader(file, delimiter=',')
        # for row in reader:
        #     print(row)  # TODO считать содержимое csv файла
        with open(OUTPUT_FILENAME, 'w') as f:
            # json_string = json.dumps(list(reader), indent=4)
            # f.write(json_string)
            json.dump(list(reader), f, indent=4)
        # return json_string





if __name__ == '__main__':
    # Нужно для проверки
    task()

with open(OUTPUT_FILENAME) as output_f:
    for line in output_f:
        print(line, end="")
