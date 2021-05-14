import paho.mqtt.client as mqtt

'''
    Abstract wrapper class for the MQTT protocol. 
    
    Requires the following dependencies:
       1) paho-mqtt: python3 -m pip install paho-mqtt
'''
class MQTTWrapper:

    '''
        Constructor for the MQTTWrapper class.
        @param broker: IP Address of the MQTT broker.
    '''
    def __init__(self, broker):
        self.brokerIP = broker
        self.topics = []
        self.client = mqtt.Client()

    '''
        Callback function that is defined in the library.
        function executes when the client receives a CONNACK from broker.
        @param client: client instances in client / broker relationship.
        @param userdata: user defined data that is passed as "userdata" to callbacks.
        @param flags: a dict that contains response flags from the broker
        @param rc: Determines success or not.
                 |      0: Connection successful
                 |      1: Connection refused - incorrect protocol version
                 |      2: Connection refused - invalid client identifier
                 |      3: Connection refused - server unavailable
                 |      4: Connection refused - bad username or password
                 |      5: Connection refused - not authorised
    '''
    def on_connect(self, client, userdata, flags, rc):
        for topic in self.topics:
            self.client.subscribe(topic)


    '''
        Abstract Callback function that is defined in the library.
        function executes when the client receives a
        PUBLISH message from the server.
        @param client: client instances in client / broker relationship.
        @param userdata:
        @param msg: MQTTMessage that describes all of the message parameters.
    '''
    def on_message(self, client, userdata, msg):
        pass


    '''
        Publishes a message to the broker pertaining to a given topic.
        @param client: client instances in client / broker relationship.
        @param topic: The topic that the message should be published on.
        @param payload: The actual message to send.
                        Passing an int or float will result in the payload
                        being converted to a string representing that number.
        @return: Instance of MQTTMessageInfo class which can be used to determine
                 success of message publish.
    '''
    def publish(self, client, topic, payload):
        success = ''

        try:
            success = client.publish(topic, payload)
        except Exception as e:
            print("Publish has failed.\n{}".format(str(e)))

        return success
