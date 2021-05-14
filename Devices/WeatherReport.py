from requests import get
from datetime import datetime
from Devices.Device import Device

'''
    Responsible for retrieving the daily and weekly weather results.
    Uses the National Weather Services REST API.
    
    Inherits from the Device abstract class.
'''
class WeatherReport(Device):

    '''
        Constructor for the WeatherReport class.
    '''
    def __init__(self):
        super().__init__('WeatherReport', 'Started')
        self.SevenDays = dict()
        self.latestResults = dict()
        self.topic = 'WeatherReport'
        self.URL = 'https://api.weather.gov/gridpoints/RAH/68,75/forecast'
        self.lastQueryTime = datetime.strptime('1970-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')

    '''
        Retrieves the daily weather forecast.
        @return: Overview of the daily forecast, including temp and expected weather.
    '''
    def QueryDailyWeather(self):
        current_time = datetime.now()

        # If last REST API call has been at least a day ago.
        if (current_time - self.lastQueryTime).days >= 1:
            results = get(self.URL)
            self.lastQueryTime = current_time.strftime('%Y-%m-%d %H:%M:%S')

            try:
                self.latestResults = results.json()['properties']['periods'][0]
            except Exception as e:
                pass

        return self.latestResults['detailedForecast']


    '''
        Retrieves the weekly weather forecast.
    '''
    def SevenDayForecast(self):
        results = get(self.URL)

        try:
            self.SevenDays = [results.json()['properties']['periods'][i] for i in range(0, 6)]
        except:
            pass

        return ''.join([k['name'], ',', k['detailedForecast'], '.', ' '] for k in self.SevenDays)
