import cherrypy
import json
import time
from discography import Discography

class webdisc(object):
	exposed = True

	def __init__(self):
		self.disc = Discography()

	def GET (self, *uri, ** params):
		command = uri[0] # name of the method
		fp = open("discography.txt")
		dd = json.loads(fp.read())				# dictionary for the discography

		# use the dictionary to store the parameters for the query
		dd["a"] = params["artist"].replace('_', ' ')
		dd["t"] = params["title"].replace('_', ' ')
		dd["py"] = int(params["py"])
		dd["tt"] = int(params["tt"])
		
		# map the input string into methods
		methods = {"print_all": self.disc.print_all, 
		"search_by_artist": self.disc.search_by_artist,
		"search_by_title": self.disc.search_by_title,
		"search_by_publication_year": self.disc.search_by_publication_year,
		"search_by_total_tracks": self.disc.search_by_total_tracks}
		
		result = methods[command](dd)
		fp.close()
		return result

	def POST(self):
		# file with the whole discography
		filename = "discography.txt"
		fp = open(filename)
		dict_file = json.loads(fp.read())				# dictionary for the discography
		
		# html body with the new album (JSON string)
		dict_body = json.loads(cherrypy.request.body.read())	# dictionary for the new album
		dict_file["a"] = dict_body["artist"]			# same way of before, in GET
		dict_file["t"] = dict_body["title"]
		dict_file["py"] = dict_body["publication_year"]
		dict_file["tt"] = dict_body["total_tracks"]		

		new_dd = self.disc.insert_a_new_album(dict_file)
		if not new_dd["updated"] :
			# remove the old variables 
			new_dd.pop("a")
			new_dd.pop("t")
			new_dd.pop("py")
			new_dd.pop("tt")
			new_dd.pop("updated")

			fp.close()
			fp = open(filename, 'w')								# truncate() doesn't work with open(filename, 'r+')
			fp.write(json.dumps(new_dd))
 			return "A new album has been added."
		else:
 			return "The album already exists. 'last_update' field has been updated!"
		fp.close()

	def DELETE(self, *uri, ** params):
		# file with the whole discography
		filename = "discography.txt"
		fp = open(filename)
		dict_file = json.loads(fp.read())				# dictionary for the discography

		# # html body with the album (JSON string) that has to be deleted
		# dict_body = json.loads(cherrypy.request.body.read())	# dictionary for the new album
		dict_file["a"] = params["artist"]			# same way of before, in GET
		dict_file["t"] = params["title"]
		dict_file["py"] = params["py"]
		dict_file["tt"] = params["tt"]	
			
		new_dict_file = self.disc.delete_album(dict_file)
		if new_dict_file["deleted"] :
			# remove the old variables 
			new_dict_file.pop("a")
			new_dict_file.pop("t")
			new_dict_file.pop("py")
			new_dict_file.pop("tt")
			new_dict_file.pop("deleted")
			
			fp.close()
			fp = open(filename, 'w')								# truncate() doesn't work with open(filename, 'r+')
			fp.write(json.dumps(new_dict_file))
 			return "The album has been deleted."
		else:
 			return "The album doesn't exist."
		fp.close()
		

if __name__ == "__main__":
	conf = {
		'/': {
			'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
			'tools.sessions.on': True,
		}
	}  
	cherrypy.quickstart(webdisc(), '/', conf)
