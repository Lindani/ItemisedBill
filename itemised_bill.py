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


def itemised_bill_provider_numbers(listOfMaps, provider):
    call_list = []
    for network in listOfMaps:
        if network['Provider'] == provider:
            call_list.append(network['Number'])
    return call_list
