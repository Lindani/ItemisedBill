import csv
import datetime
import time


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


# def itemised_bill_call_numbers_per_provider(listOfMaps):
#     # myDict = {}
#     for row in listOfMaps:
#         # network = row['MTN']

#         # if myDict[network] is None:
#         #     myDict[network].count(call)
#         return row
# def itemised_bill_call_numbers_per_provider(listOfMaps):
#     call_list = []
#     for network in listOfMaps:
#             call_list.append(network['Number'])
#     myDict = {}
#     for mylist in call_list:
#         if myDict[myDict] is None:
#             myDict[myDict] = 0
#         myDict += 1

#     return myDict
def itemised_bill_call_duration(listOfMaps):
    mylist = []
    for rows in listOfMaps:
        mylist.append(rows['Duration'])
    return mylist[0]


def itemised_bill_duration_in_seconds(duration):
    return int(duration[0:2]) * 3600 + int(duration[3:5]) * 60 + int(duration[6:8])
