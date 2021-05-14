from MQTT.MQTTWrapper import MQTTWrapper

'''
    Abstract class that represents a single IoT device / functionality.
    
    The Device class inherits the properties of the MQTTWrapper class 
    to allow for child devices to control which MQTT topics are subscribed
    or published to. 
'''
class Device(MQTTWrapper):

    '''
        Constructor for the Device Abstract class.
    '''
    def __init__(self, name, status):
        super().__init__('192.168.1.13')
        self.name = name
        self.status = status

    '''
        Abstract method used to update similar devices.
        Devices are updated based on MQTT topic.
    '''
    def UpdateDevices(self, client, topic):
        pass