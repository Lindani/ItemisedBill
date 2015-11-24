import csv


def itemised_bill():

    items = open('ItemisedBill.csv', 'rU')
    csv_items = csv.reader(items)
    for i in csv_items:
        print i
itemised_bill()


# with open('ItemisedBill.csv', 'rU') as csvfile:
#     spamreader = csv.reader(csvfile)
#     for i in spamreader:
#         print i
