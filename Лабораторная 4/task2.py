import csv

import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(separator=',', line_terminator='\n') -> None:
        with open(INPUT_FILENAME, mode='r', newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=separator)
            data = [row for row in reader]

        with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        with open(OUTPUT_FILENAME, 'r', encoding='utf-8') as output_f:
            json_data = output_f.read()
            print(json_data)



if __name__ == '__main__':
    task()


