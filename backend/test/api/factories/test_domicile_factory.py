import unittest
from src.api.factories.domicile_factory import DomicileFactory


class TestDomicileFactory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.domicile_factory = DomicileFactory()
        cls.mocked_domicile = {
            'streetAddress': 'Calle',
            'streetNumber': '1234',
            'city': 'Ciudad',
            'floor': '',
            'postalCode': '1111',
            'country': 'AR'
        }

    @classmethod
    def tearDownClass(cls):
        pass

    def test_creation(self):
        domicile = self.domicile_factory.create(self.mocked_domicile)
        self.assertEqual(domicile.street_address, 'Calle', 'Should be Calle')
        self.assertEqual(domicile.street_number, '1234', 'Should be 1234')
        self.assertEqual(domicile.city, 'Ciudad', 'Should be Ciudad')
        self.assertEqual(domicile.floor, '', 'Should be ""')
        self.assertEqual(domicile.postal_code, '1111', 'Should be 1111')
        self.assertEqual(domicile.country, 'AR', 'Should be Argentina')


if __name__ == '__main__':
    unittest.main()
