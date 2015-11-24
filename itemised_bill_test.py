from itemised_bill import itemised_bill
import unittest


class MyTest(unittest.TestCase):

    def setUp(self):
        self.data = 'ItemisedBill.csv'

    def test_itemised_bill_headers(self):

        self.assertEqual(itemised_bill(self.data)[0],
                         ['Date', 'Provider', 'Number', 'Duration'])

    def test_itemised_bill_data(self):
        self.assertEqual(itemised_bill(self.data)[1][0], '01/10/2015')
        self.assertEqual(itemised_bill(self.data)[1][1], 'MTN')
        self.assertEqual(itemised_bill(self.data)[1][2], '0832401145')
if __name__ == '__main__':
    unittest.main()
