class Discography():

	# return False if there is no match
	def search_by_artist(self, a, d):
		result = ""
		for i in range(len(d["album_list"])):								# index for the albums
			if a == d["album_list"][i]["artist"]:
				result += "-> Title: "
				result += d["album_list"][i]["title"] 
				result += ", Publication Year: "
				result += str(d["album_list"][i]["publication_year"])
				result += ", Total Tracks: "
				result += str(d["album_list"][i]["total_tracks"]) 
				result += "\n"

 		return result

	def search_by_title(self, t, d):
		result = ""
		for i in range(len(d["album_list"])):								# index for the albums
			if t == d["album_list"][i]["title"]:
				result += "-> Artist: "
				result += d["album_list"][i]["artist"] 
				result += ", Publication Year: "
				result += str(d["album_list"][i]["publication_year"])
				result += ", Total Tracks: "
				result += str(d["album_list"][i]["total_tracks"]) 
				result += "\n"
 		return result

	def search_by_publication_year(self, py, d):
		result = ""
		for i in range(len(d["album_list"])):								# index for the albums
			if py == d["album_list"][i]["publication_year"]:
				result += "-> Artist: "
				result += d["album_list"][i]["artist"] 
				result += ", Title: "
				result += d["album_list"][i]["title"]
				result += ", Total Tracks: "
				result += str(d["album_list"][i]["total_tracks"]) 
				result += "\n"
 		return result

	def search_by_total_tracks(self, tt, d):
		result = ""
		for i in range(len(d["album_list"])):								# index for the albums
			if tt == d["album_list"][i]["total_tracks"]:
				result += "-> Artist: "
				result += d["album_list"][i]["artist"] 
				result += ", Title: "
				result += d["album_list"][i]["title"]
				result += ", Publication Year: "
				result += str(d["album_list"][i]["publication_year"])
				result += "\n"
 		return result

 	def insert(self, a, t, py, tt, d):
 		# if the album already exists
 		if self.search_by_artist(a, d) and self.search_by_title(t, d) and self.search_by_total_tracks(tt, d) and self.search_by_publication_year(py, d):
 			print "This album already exists. Do you want to update it? y/n"
 			ans = raw_input("> ")
 			if ans == "y":
 				d["last_update"] = time.strftime("%Y-%m-%d %H:%M")
 				print "\n last_update field has been updated!"
 		else:
 			new_sub_d = {"artist": a, "title": t, "publication_year": py, "total_tracks": tt}
 			d["album_list"].append(new_sub_d)
 			print "A new album has been added to the list."
 		return d
 			# result = str(type(d["album_list"]))					LIST
 			# result += str(type(d["album_list"][3]))				DICT
 			# result += str(type(d["album_list"][3]["title"]))		UNICODE

 	def print_all(self, d):
		result = ""
 		for i in range(len(d["album_list"])):								# index for the albums
			result += "Artist: " + d["album_list"][i]["artist"] 
			result += ", Title: " + d["album_list"][i]["title"]
			result += ", Publication Year: " + str(d["album_list"][i]["publication_year"])
			result += " ,Total Tracks: " + str(d["album_list"][i]["total_tracks"]) 		
			result += "-" * 30
		return result