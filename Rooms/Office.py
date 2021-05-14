from requests import post
from Rooms.Room import Room
from Devices.WeatherReport import WeatherReport

'''
    Represents an office-type room. 
    Controls all IoT devices contained in an Office. 
    Inherits from the Room abstract class. 
'''
class Office(Room):

    '''
        Constructor for the Office class.
    '''
    def __init__(self):
        self.location = 'Office'
        self.devices = {'WeatherReport': WeatherReport('Office')}


    '''
        Retrieves all associated devices as well as their current
        operational status.
        @return: Dictionary containing all associated devices and
                 their status.
    '''
    def getDevices(self):
        return [{'Device': key, 'Status': self.devices[key].status} for key in self.devices]
