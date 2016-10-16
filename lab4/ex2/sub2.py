import paho.mqtt.client as mqtt
import json

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("ex2/2")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	content = str(msg.payload)
	d = json.loads(content)
	print("Topic: " + msg.topic + ", Message: " + str(d["timestamp"]))

sub2 = mqtt.Client("sub2", False)
sub2.on_connect = on_connect
sub2.on_message = on_message

sub2.connect("localhost")

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
sub2.loop_forever()