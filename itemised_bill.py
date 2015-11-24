import csv


def itemised_bill(data):

    with open(data, 'r') as f:
        data = [row for row in csv.reader(f.read().splitlines())]
    return data
