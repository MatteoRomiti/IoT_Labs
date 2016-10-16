import paho.mqtt.client as mqtt
import time

pub1 = mqtt.Client("pub1")
pub1.connect("localhost")
pub1.loop_start()

n = 0
while True:
	ts = int(time.time())
	msg1 = '{"timestamp": ' + str(ts) + '}'   
	pub1.publish("ex2/2", msg1)

	n += 1
	if n == 2:
		dt = time.strftime("%d-%m-%Y %H:%M")
		msg2 = '{"datetime": "' + str(dt) + '"}'
		pub1.publish("ex2/1", msg2)
		n = 0

	time.sleep(30)