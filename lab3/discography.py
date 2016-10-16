import time

class Discography(object):

	# return False in d["deleted"] if no album has been deleted
	def delete_album(self, d):
		d["deleted"] = False
		for i in range(len(d["album_list"])):		# index for the albums
			# find where it is
			if d["a"] == d["album_list"][i]["artist"] and d["t"] == d["album_list"][i]["title"] and int(d["tt"]) == d["album_list"][i]["total_tracks"] and int(d["py"]) == d["album_list"][i]["publication_year"]:
				d["album_list"].pop(i) 
				d["deleted"]  = True
				break		# if the album is found and deleted, the for loop ends
		return d
 		
	def search_by_artist(self, d):
		result = ""
		for i in range(len(d["album_list"])):								# index for the albums
			if d["a"] == d["album_list"][i]["artist"]:		# compare the input artist with the artists in the discography
				result += "-> Title: "
				result += d["album_list"][i]["title"] 
				result += ", Publication Year: "
				result += str(d["album_list"][i]["publication_year"])
				result += ", Total Tracks: "
				result += str(d["album_list"][i]["total_tracks"]) 
				result += "\n"
		if result:
 			return result
 		else:
 			return "Sorry, artist not found"

	# return False if there is no match
	def search_by_artist_post(self, d):
		result = ""
		for i in range(len(d["album_list"])):								# index for the albums
			if d["a"] == d["album_list"][i]["artist"]:		# compare the input artist with the artists in the discography
				result += "-> Title: "
				result += d["album_list"][i]["title"] 
				result += ", Publication Year: "
				result += str(d["album_list"][i]["publication_year"])
				result += ", Total Tracks: "
				result += str(d["album_list"][i]["total_tracks"]) 
				result += "\n"
		return result

	def search_by_title(self, d):
		result = ""
		for i in range(len(d["album_list"])):								# index for the albums
			if d["t"] == d["album_list"][i]["title"]:
				result += "-> Artist: "
				result += d["album_list"][i]["artist"] 
				result += ", Publication Year: "
				result += str(d["album_list"][i]["publication_year"])
				result += ", Total Tracks: "
				result += str(d["album_list"][i]["total_tracks"]) 
				result += "\n"
		if result:
 			return result
 		else:
 			return "Sorry, title not found"
	
	# return False if there is no match
	def search_by_title_post(self, d):
		result = ""
		for i in range(len(d["album_list"])):								# index for the albums
			if d["t"] == d["album_list"][i]["title"]:
				result += "-> Artist: "
				result += d["album_list"][i]["artist"] 
				result += ", Publication Year: "
				result += str(d["album_list"][i]["publication_year"])
				result += ", Total Tracks: "
				result += str(d["album_list"][i]["total_tracks"]) 
				result += "\n"
		return result

	def search_by_publication_year(self, d):
		result = ""
		for i in range(len(d["album_list"])):								# index for the albums
			if d["py"] == d["album_list"][i]["publication_year"]:
				result += "-> Artist: "
				result += d["album_list"][i]["artist"] 
				result += ", Title: "
				result += d["album_list"][i]["title"]
				result += ", Total Tracks: "
				result += str(d["album_list"][i]["total_tracks"]) 
				result += "\n"
		if result:
 			return result
 		else:
 			return "Sorry, publication year not found"

	# return False if there is no match
	def search_by_publication_year_post(self, d):
		result = ""
		for i in range(len(d["album_list"])):								# index for the albums
			if d["py"] == d["album_list"][i]["publication_year"]:
				result += "-> Artist: "
				result += d["album_list"][i]["artist"] 
				result += ", Title: "
				result += d["album_list"][i]["title"]
				result += ", Total Tracks: "
				result += str(d["album_list"][i]["total_tracks"]) 
				result += "\n"
 		return result

	def search_by_total_tracks(self, d):
		result = ""
		for i in range(len(d["album_list"])):								# index for the albums
			if d["tt"] == d["album_list"][i]["total_tracks"]:
				result += "-> Artist: "
				result += d["album_list"][i]["artist"] 
				result += ", Title: "
				result += d["album_list"][i]["title"]
				result += ", Publication Year: "
				result += str(d["album_list"][i]["publication_year"])
				result += "\n"
		if result:
 			return result
 		else:
 			return "Sorry, total tracks not found"

	# return False if there is no match
	def search_by_total_tracks_post(self, d):
		result = ""
		for i in range(len(d["album_list"])):								# index for the albums
			if d["tt"] == d["album_list"][i]["total_tracks"]:
				result += "-> Artist: "
				result += d["album_list"][i]["artist"] 
				result += ", Title: "
				result += d["album_list"][i]["title"]
				result += ", Publication Year: "
				result += str(d["album_list"][i]["publication_year"])
				result += "\n"
 		return result

	# return False in d["updated"] if the album already exists
 	def insert_a_new_album(self, d):
		d["updated"] = False
		for i in range(len(d["album_list"])):		# index for the albums
			# find if it already exists and update it
			if d["a"] == d["album_list"][i]["artist"] and d["t"] == d["album_list"][i]["title"] and d["t"] == d["album_list"][i]["title"] and d["py"] == d["album_list"][i]["publication_year"]:
				d["last_update"] = time.strftime("%Y-%m-%d %H:%M")
				d["updated"] = True
 		if not d["updated"]: # if no album has been updated
 			new_sub_d = {"artist": d["a"], "title": d["t"], "publication_year": d["py"], "total_tracks": d["tt"]}
 			d["album_list"].append(new_sub_d)
 		return d
 			# result = str(type(d["album_list"]))					LIST
 			# result += str(type(d["album_list"][3]))				DICT
 			# result += str(type(d["album_list"][3]["title"]))		UNICODE

 	def print_all(self, d):
		result = ""
 		for i in range(len(d["album_list"])):								# index for the albums
			result += "\n Artist: " + d["album_list"][i]["artist"] 
			result += "\n Title: " + d["album_list"][i]["title"]
			result += "\n Publication Year: " + str(d["album_list"][i]["publication_year"])
			result += "\n Total Tracks: " + str(d["album_list"][i]["total_tracks"]) 		
			result += "\n"
			result += "-" * 30
		return result