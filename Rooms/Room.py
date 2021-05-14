'''
    Abstract class that represents a single room
    that contains one or more IoT devices.
'''
class Room:

    '''
        Constructor for the Room abstract class.
    '''
    def __init__(self):
        self.devices = []
        self.location = ''
        self.strength = 0
        self.command = ''

    def searchForDevice(self):
        pass

    '''
        Polls the room listening for a command from a user.
    '''
    def detectCommand(self):
        pass