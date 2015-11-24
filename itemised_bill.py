import csv


def itemised_bill(data):

    with open(data, 'r') as f:
        data = [row for row in csv.reader(f.read().splitlines())]
    return data


def itemised_bill_list_of_maps(value):

    key = ['Date', 'Provider', 'Number', 'Duration']
    dictList = []
    for values in value:
        dictList.append(dict(zip(key, values)))
    return dictList
