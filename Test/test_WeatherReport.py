import unittest
from Devices.WeatherReport import WeatherReport

'''
    Tests the functionality of the WeatherReport class.
'''
class MyTestCase(unittest.TestCase):

    '''
        Initializes variables used for testing.
    '''
    def setUp(self):

        self.WR = WeatherReport()

    '''
        Tests the functionality of the WeatherReport constructor
    '''
    def test_Constructor(self):
        self.assertIsNotNone(self.WR)
        self.assertEqual(self.WR.lastQueryTime.strftime('%Y-%m-%d %H:%M:%S'), '1970-01-01 00:00:00')
        self.assertEqual(self.WR.topic, 'WeatherReport')
        self.assertEqual(self.WR.URL, 'https://api.weather.gov/gridpoints/RAH/68,75/forecast')


    '''
        Tests the functionality of the QueryDailyWeather constructor
    '''
    def test_QueryDailyWeather(self):
        self.WR.QueryDailyWeather()

        # Make sure API Call succeeded
        self.assertNotEqual(self.WR.lastQueryTime, '')
        self.assertNotEqual(len(self.WR.latestResults), 0)

        # Check returned contents
        keys = ['number', 'name', 'startTime', 'endTime', 'isDaytime', 'temperature',
                'temperatureUnit', 'temperatureTrend', 'windSpeed', 'windDirection',
                'icon', 'shortForecast', 'detailedForecast']
        result_keys = self.WR.latestResults.keys()

        for key in keys:
            self.assertTrue(key in result_keys)

        self.assertEqual(len(keys), len(result_keys))


if __name__ == '__main__':
    unittest.main()
