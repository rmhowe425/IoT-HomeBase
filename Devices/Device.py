'''
    Abstract class that represents a single IoT device / functionality.
'''
class Device:

    '''
        Constructor for the Device Abstract class.
    '''
    def __init__(self, name, status):
        self.name = name
        self.Status = status

    '''
        Abstract method used to update similar devices.
        Devices are updated based on MQTT topic.
    '''
    def UpdateDevices(self, client, topic):
        pass