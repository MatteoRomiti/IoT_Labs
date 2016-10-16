import json
import datetime
import Adafruit_DHT
import time

class Sensor(object):

	def get_temperature_info(self):
		hum, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHTpin, 5, 2)
		if temp is not None:
			ts = int(time.time())
			res = '{"bn": "DHT11","bt": ' + str(ts) + ' ,"e": [{"n": "Temperature","u": "Celsius Degrees","v": ' + str(temp) + '}]}'
			# fp = open("sensor1.txt")
			# d = json.loads(fp.read())
			# res  = "Name: " + d["bn"]
			# res += ", Unix Timestamp: " + d["bt"]
			# dt = datetime.datetime.fromtimestamp(int(d["bt"])).strftime("%d-%m-%Y %H:%M:%S")
			# res += ", Date ant Time: " + dt
			# res += ", Temperature: " + d["e"][0]["v"] + " " + d["e"][0]["u"]
			# fp.close()
			# return res

			return res
		else:
			return "Error"

	def get_humidity_info(self):
		hum, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHTpin, 5, 2)
		if hum is not None:
			ts = 
			res = '{"bn": "DHT11","bt": ' + str(ts) + ' ,"e": [{"n": "Humidity","u": "%","v": ' + str(hum) + '}]}'

		# fp = open("sensor1.txt")
		# d = json.loads(fp.read())
		# res  = "Name: " + d["bn"]
		# res += ", Unix Timestamp: " + d["bt"]
		# dt = datetime.datetime.fromtimestamp(int(d["bt"])).strftime("%d-%m-%Y %H:%M:%S")
		# res += ", Date ant Time: " + dt
		# res += ", Humidity: " + d["e"][1]["v"] + " " + d["e"][1]["u"]
		# fp.close()
		# return res

			return res
		else:
			return "Error"
	# WORK IN PROGRESS
	def get_relay_status(self):
		pass
		# fp = open("relay.txt")
		# d = json.loads(fp.read())
		# res  = "Name: " + d["bn"]
		# res += ", Unix Timestamp: " + d["bt"]
		# dt = datetime.datetime.fromtimestamp(int(d["bt"])).strftime("%d-%m-%Y %H:%M:%S")
		# res += ", Date ant Time: " + dt
		# res += ", Status: " + d["e"][0]["v"]
		# fp.close()
		# return res

	# WORK IN PROGRESS
	def toggle_relay_status(self):
		# do something with the RPi.GPIO library and update relay.txt
		# return "Relay Status toggled"
		pass