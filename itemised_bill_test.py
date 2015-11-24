from itemised_bill import itemised_bill, itemised_bill_list_of_maps
import unittest


class MyTest(unittest.TestCase):

    def setUp(self):
        self.data = 'ItemisedBill.csv'

    def test_itemised_bill_data(self):

        self.assertEqual(itemised_bill(self.data)[0],
                         ['01/10/2015', 'MTN', '0832401145', '00h05m34s'])

    def test_itemised_bill_list_of_map(self):
        results = itemised_bill(self.data)
        self.assertEqual(itemised_bill_list_of_maps(results)[0],
                         {'Date': '01/10/2015',
                          'Duration': '00h05m34s',
                          'Number': '0832401145',
                          'Provider': 'MTN'})

if __name__ == '__main__':
    unittest.main()
