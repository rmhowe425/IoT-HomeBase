import unittest
from Rooms.Office import Office
from Devices.WeatherReport import WeatherReport

'''
    Tests the functionality of the Office class.
'''
class testOffice(unittest.TestCase):

    def setUp(self):
        self.office = Office()
        self.office.devices = {'WeatherReport': WeatherReport('Office')}


    '''
        Tests the functionality of the Office Constructor
    '''
    def test_Constructor(self):
        self.assertEqual(self.office.location, 'Office')
        self.assertEqual(type(self.office.devices['WeatherReport']), type(WeatherReport('Office')))
        self.assertTrue(len(self.office.devices), 1)

    '''
        Tests the functionality of the GetDevices method.
        Retrieves Office-associated devices along with their status. 
    '''
    def test_GetDevices(self):
        results = self.office.getDevices()

        self.assertIsNotNone(results)
        self.assertTrue(len(results), 1)
        self.assertEqual(results[0]['Device'], 'WeatherReport')
        self.assertEqual(results[0]['Status'], 'Connected')

if __name__ == '__main__':
    unittest.main()
