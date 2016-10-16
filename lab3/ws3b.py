import cherrypy
import json
import urllib2
from bike_sharing2 import Bike_Sharing

class web_bike(object):
	exposed = True

	def __init__(self):
	 	self.bs = Bike_Sharing()

	def GET (self, *uri, ** params):

		if len(uri) == 1:
			user = {}			
			user["command"] = uri[0] # name of the method
		
			# default values
			user["N"] = 10
			user["order"] = 1
			user["Ne"] = 10
	
			# read the input values
			for key, value in params.items():
				user[key] = int(params[key])
	
			# get the big JSON list
			url = "https://www.bicing.cat/availability_map/getJsonObject"
			response = urllib2.urlopen(url)
			content = response.read()
			lst = json.loads(content)				# list of dictionaries

			# mapping strings to methods
			methods = {"sort_by_available_slots": self.bs.sort_by_available_slots,
			"sort_by_available_bikes": self.bs.sort_by_available_bikes,
			"select_by_zipcode": self.bs.select_by_zipcode,
			"stations_with_more_than_N_available_ebikes": self.bs.stations_with_more_than_N_available_ebikes,
			"get_the_amount_of_bikes_and_slots_in_a_district":self.bs.get_the_amount_of_bikes_and_slots_in_a_district}

			# in case of a big N
			if user["N"] > len(lst): 		
				user["N"] = len(lst)

			# if no zipcode is provided
			if user["command"] == "select_by_zipcode" and not user.has_key("zipcode"):
				return "Please, enter a zipcode"
			elif user["command"] == "get_the_amount_of_bikes_and_slots_in_a_district" and not user.has_key("district"):
				return "Please, enter a district number"
			else: 
				new_list = methods[user["command"]](lst, user)
				JSON_list = json.dumps(new_list)
				return JSON_list
		else:
			return """
				Choose one option: <br \>
				sort_by_available_slots (by default: 10 stations in descending order) <br \>
				sort_by_available_bikes (by default: 10 stations in descending order) <br \>
				select_by_zipcode (zipcode is mandatory) <br \>
				stations_with_more_than_N_available_ebikes (by default: N = 10) <br \>
				get_the_amount_of_bikes_and_slots_in_a_district (district is mandatory) <br \>
				"""
		# try:
		# 	# use a dict to store the user's inputs
		# 	user["command"] = uri[0] # name of the method
		# 	user["N"] = int(params["N"])
		# 	user["order"] = int(params["order"])
		# 	user["zipcode"] = int(params["zipcode"])
		# 	user["Ne"] = int(params["Ne"])
		# 	user["district"] = int(params["district"])
		# except:
		# 	pass






if __name__ == "__main__":
	conf = {
		'/': {
			'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
			'tools.sessions.on': True,
		}
	}  
	cherrypy.quickstart(web_bike(), '/', conf)
