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
        @param room: Room that the device belongs to.
    '''
    def __init__(self, room):
        super().__init__('WeatherReport', 'Started')
        self.room = room
        self.update = False
        self.SevenDays = dict()
        self.latestResults = dict()
        self.topics = ['Device/WeatherReport/DailyUpdate']
        self.URL = 'https://api.weather.gov/gridpoints/RAH/68,75/forecast'
        self.lastQueryTime = datetime.strptime('1970-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')


    '''
        Retrieves the daily weather forecast.
        @return: Overview of the daily forecast, including temp and expected weather.
    '''
    def QueryDailyWeather(self):
        pub_topic = 'Device/WeatherReport/DailyUpdate'
        payload = {'Device': self.name, 'Weather': ''}

        # If last REST API call has been at least a day ago.
        if not self.update:
            results = get(self.URL)
            self.lastQueryTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            try:
                self.latestResults = results.json()['properties']['periods'][0]
                payload['Weather'] = self.latestResults['detailedForecast']
            except Exception as e:
                pass

        self.publish(self.client, pub_topic, payload)



    '''
        Retrieves the weekly weather forecast using the NWS REST API. 
        @return: 7 day forecast. 
    '''
    def SevenDayForecast(self):
        results = get(self.URL)
        pub_topic = 'Device/WeatherReport/WeeklyDailyUpdate'
        payload = {'Device': self.name, 'Weather': ''}

        try:
            self.SevenDays = [results.json()['properties']['periods'][i] for i in range(0, 6)]
            payload['Weather'] = ''.join([k['name'], ',', k['detailedForecast'], '.', ' ']
                                         for k in self.SevenDays)
        except Exception as e:
            pass

        self.publish(self.client, pub_topic, payload)


    '''
        Overrides the MQTTWrapper on_message abstract function.
        Determines the functionality to be executed when a subscribed topic
        receives a message. 
        @param client: MQTT client.
        @param userdata: User defined data that is passed as "userdata" to callbacks.
        @param msg: MQTT Message being received. 
    '''
    def on_message(self, client, userdata, msg):
        topic = msg.topic

        # Verifies that the daily weather update has been received.
        if topic == 'Device/WeatherReport/DailyUpdate':
            self.update = True


    '''
        Sends a daily update regarding the 
        working status of the device. 
        @param client: Instance of MQTT client.
        @param topic: Topic to publish on. 
    '''
    def UpdateDevices(self, client, topic):
        pub_topic = 'Room/Device/Status/Update'
        payload = {'Room': self.room, 'Device': self.name, 'Status': self.status}
        self.publish(self.client, pub_topic, payload)
