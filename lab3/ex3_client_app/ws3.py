import cherrypy
import json
import urllib2
from bike_sharing import Bike_Sharing

class web_bike(object):
	exposed = True

	def __init__(self):
	 	self.bs = Bike_Sharing()

	def GET (self, *uri, ** params):
		# use a dict to store the user's inputs
		user = {}
		user["command"] = uri[0] # name of the method
		user["n"] = int(params["n"])
		user["order"] = int(params["order"])
		user["zipcode"] = int(params["zipcode"])
		user["ne"] = int(params["ne"])
		user["district"] = int(params["district"])
		
		# get the big JSON list
		url = "https://www.bicing.cat/availability_map/getJsonObject"
		response = urllib2.urlopen(url)
		content = response.read()
		lst = json.loads(content)				# list of dictionaries

		# mapping strings to methods
		methods = {"sort_by_available_slots": self.bs.sort_by_available_slots,
		"sort_by_available_bikes": self.bs.sort_by_available_bikes,
		"select_by_zipcode": self.bs.select_by_zipcode,
		"stations_with_more_than_n_available_ebikes": self.bs.stations_with_more_than_n_available_ebikes,
		"get_the_amount_of_bikes_and_slots_in_a_district":self.bs.get_the_amount_of_bikes_and_slots_in_a_district}

		# fp = open("jsonbikes.txt")
		# content = fp.read()
		# fp = open("jsonbikes.txt")

		# in case of a big N
		if user["n"] > len(lst): 		
			user["n"] = len(lst)

		new_lst = methods[user["command"]](lst, user)

		result = "\n-----------\n"
		for i in range(len(new_lst)):
			result += str(new_lst[i])

		# 	result += "id = " + new_lst[i]["id"] + "\n"
		# 	result += "district = " + str(new_lst[i]) + "\n" # ["district"]
		# 	result += "lon = " + new_lst[i]["lon"] + "\n"
		# 	result += "lat = " + new_lst[i]["lat"] + "\n"
		# 	result += "bikes = " + str(new_lst[i]["bikes"]) + "\n"
		# 	result += "slots = " + str(new_lst[i]["slots"]) + "\n"
		# 	result += "zip = " + new_lst[i]["zip"] + "\n"
		# 	result += "address = " + new_lst[i]["address"] + "\n"
		# 	# not all the dictionaries have an addressNumber
		# 	if new_lst[i].has_key("addressNumber"):
		# 		result += "addressNumber = " + new_lst[i]["addressNumber"] + "\n"
		# 	result += "nearbyStations = " + new_lst[i]["nearbyStations"] + "\n"
		# 	result += "status = " + new_lst[i]["status"] + "\n"
		# 	result += "name = " + new_lst[i]["name"] + "\n"
		# 	result += "stationType = " + new_lst[i]["stationType"] + "\n"
			result += "\n-----------\n"
		return result

if __name__ == "__main__":
	conf = {
		'/': {
			'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
			'tools.sessions.on': True,
		}
	}  
	cherrypy.quickstart(web_bike(), '/', conf)
