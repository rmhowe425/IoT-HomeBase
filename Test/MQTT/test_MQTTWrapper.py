import unittest
from MQTT.MQTTWrapper import MQTTWrapper

'''
    Tests the functionality of the MQTTWrapper class.
'''
class TestMQTTWrapper(unittest.TestCase):

    '''
        Initializes variables used throughout the test case.
    '''
    def setUp(self):
        self.mqtt = MQTTWrapper('192.168.1.1')

    '''
        Tests the functionality of the constructor for the MQTTWrapper class. 
    '''
    def test_Constructor(self):
        self.assertIsNotNone(self.mqtt.client)
        self.assertEqual(self.mqtt.topics, list())
        self.assertEqual(self.mqtt.brokerIP, '192.168.1.1')




if __name__ == '__main__':
    unittest.main()
