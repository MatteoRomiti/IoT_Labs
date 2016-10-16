import cherrypy
import json
from sensor import Sensor

class websensor(object):
	exposed = True

	def __init__(self):
		self.sens = Sensor()

	def GET (self, *uri, ** params):
		if len(uri) == 1:
			actions = ["get_temperature_info", "get_humidity_info", "toggle_relay_status", "get_relay_status"]
			if uri[0] in actions:
				command = uri[0] # name of the method

				# map the input string into methods
				methods = {"get_temperature_info": self.sens.get_temperature_info, 
				"get_humidity_info": self.sens.get_humidity_info,
				"toggle_relay_status": self.sens.toggle_relay_status,
				"get_relay_status": self.sens.get_relay_status}
				
				result = methods[command]()
		
				return result
			else: 
				return "Invalid query"
		else:
			return "Invalid url"

if __name__ == "__main__":
	conf = {
		'/': {
			'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
			'tools.sessions.on': True,
		}
	}  
	cherrypy.quickstart(websensor(), '/', conf)
