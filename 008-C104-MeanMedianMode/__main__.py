# 004-C104-MeanMedianMode
# This is a python script made by @somePythonProgrammer 
# for a WhiteHat Junior project.

import csv
from collections import Counter

def mean(numbers: list) -> float:
    return sum(numbers) / len(numbers)

def median(numbers: list) -> float:
    numbers.sort()
    if len(numbers) % 2 == 0:
        return (numbers[int(len(numbers)/2)] + numbers[int(len(numbers)/2)-1]) / 2
    else:
        return numbers[int(len(numbers)/2)]

def mode(numbers, ranges: list) -> float:
    ranges_dict = {}
    for value in ranges:
        ranges_dict[value] = 0

    for value, occours in numbers.items():
        for range in ranges:
            range_low = int(range.split("-")[0])
            range_high = int(range.split("-")[1])
            
            if range_low<value<range_high:
                ranges_dict[range] += occours

    _range, _occours = 0,0
    for range, occours in ranges_dict.items():
        if occours > _occours:
            _range, _occours = [int(range.split("-")[0]),int(range.split("-")[1])], occours

    return float((_range[0]+_range[1])/2)

def main(csv_path: str) -> None:
    numbers = []
    ranges = [
        "0-9",
        "10-19",
        "20-29",
        "30-39",
        "40-49",
        "50-59",
        "60-69",
        "70-79",
        "80-89",
        "90-99",
        "100-109",
        "110-119",
        "120-129",
        "130-139",
        "140-149",
        "150-159",
        "160-169",
        "170-179",
        "180-189",
        "190-199",
        "200-209",
        "210-219",
        "220-229",
        "230-239",
        "240-249",
        "250-259",
    ]

    with open(csv_path, newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            try:
                numbers.append(float(row[2]))
            except:
                pass

    print("Mean:", mean(numbers))
    print("Median:", median(numbers))
    print("Mode:", mode(Counter(numbers), ranges))

if __name__ == "__main__":
    main("008-C104-MeanMedianMode/csv/height-weight.csv")
