import pandas as pd
import paho.mqtt.client as mqtt
from flask import Flask, render_template

app = Flask(__name__)
host = '192.168.1.13'
rooms = {'Office': '', 'Hallway': '', 'Bedroom': '', 'FirstFloor': ''}
df = pd.DataFrame(rooms.items(), columns = ['Location', 'Status'])

'''
    Function for Homepage.
'''
@app.route('/')
def index():
    return render_template('index.html')


'''
    Callback function that is defined in the library.
    function executes when the client receives a CONNACK from broker.
    @param client: client instances in client / broker relationship.
    @param userdata: user defined data that is passed as "userdata" to callbacks.
    @param flags: a dict that contains response flags from the broker
    @param rc: Determines success or not.
'''
def on_connect(client, userdata, flags, rc):
    for spot in rooms:
        client.subscribe(spot)

    print("Connected with result code "+str(rc))

'''
    Callback function that is defined in the library.
    function executes when the client receives a
    PUBLISH message from the server.
    @param client: client instances in client / broker relationship.
    @param userdata:
    @param msg: MQTTMessage that describes all of the message parameters.
'''
def on_message(client, userdata, msg):
    topic = msg.topic
    data = msg.payload.decode()

    if topic == 'status' and data['Room'] in df['Location'].values:
        pass


def Subscriber():
    port = 1883
    keep_alive = 60
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(host, port, keep_alive)
    client.loop_forever()


if __name__ == '__main__':
    app.run(debug = True, host = host)