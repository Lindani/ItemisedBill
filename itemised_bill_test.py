from itemised_bill import (itemised_bill,
                           itemised_bill_list_of_maps,
                           itemised_bill_provider_numbers,
                           itemised_bill_call_duration,
                           itemised_bill_duration_in_seconds)
import unittest


class MyTest(unittest.TestCase):

    def setUp(self):
        self.data = 'ItemisedBill.csv'
        self.listofLists = itemised_bill(self.data)
        self.listOfMaps = itemised_bill_list_of_maps(self.listofLists)
        self.duration = itemised_bill_call_duration(self.listOfMaps)

    def test_itemised_bill_data(self):

        self.assertEqual(itemised_bill(self.data)[0],
                         ['01/10/2015', 'MTN', '0832401145', '00h05m34s'])

    def test_itemised_bill_list_of_map(self):
        self.assertEqual(self.listOfMaps[0],
                         {'Date': '01/10/2015',
                          'Duration': '00h05m34s',
                          'Number': '0832401145',
                          'Provider': 'MTN'})

    def test_itemised_bill_provider_numbers(self):
        phone_call = itemised_bill_provider_numbers(self.listOfMaps, 'Vodacom')
        self.assertEqual(phone_call[0], '0821302398')

    # def test_itemised_bill_call_numbers_per_provider(self):
    #     number_of_calls = itemised_bill_call_numbers_per_provider(self.listOfMaps)
    #     self.assertEqual(number_of_calls, 848484)

    def test_itemised_bill_call_duration(self):
        self.assertEqual(self.duration, '00h05m34s')

    def test_itemised_bill_duration_in_seconds(self):
        duration_in_seconds = itemised_bill_duration_in_seconds(self.duration)
        self.assertEqual(duration_in_seconds, 334)

if __name__ == '__main__':
    unittest.main()
