import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    with open(INPUT_FILENAME, encoding="utf-8") as f:
        lines = [line for line in csv.DictReader(f)]

    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as f:
        json.dump(lines, f, indent=4)

if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME, encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")