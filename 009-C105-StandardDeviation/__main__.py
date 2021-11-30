# 009-C105-StandardDeviation
# This is a python script made by @somePythonProgrammer
# for a WhiteHat Junior project.

import csv

def mean(numbers: list) -> float:
    return sum(numbers) / len(numbers)

def standard_deviation(numbers):
    length = len(numbers)
    _mean = mean(numbers)

    __ = 0
    for i in range(length-1):
        __ += (numbers[i] - _mean) ** 2

    return (__ / (length - 1)) ** 0.5

if __name__ == '__main__':
    with open('009-C105-StandardDeviation/csv/data.csv', 'r') as f:
        reader = csv.reader(f)
        data = list(reader)

    print(f"Standard deviation: {standard_deviation([float(i) for i in data[0]])}")
