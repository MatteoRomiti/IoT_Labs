# discography.txt containts a json string 
# this .py file reads from and overwrites it 

import json
import time
from discography import Discography

if __name__ == "__main__":

	disc = Discography()

	what = ["search by artist", "search by title", "search by publication year", "search by total tracks", "insert a new one", "print all", "exit"]

	while True:
		
		print "What do you want to do? Choose a number: "
		for i, v in enumerate(what):
			print i, v
		raw_num = raw_input("> ")
		if raw_num.isdigit():
			num = int(raw_num)
			print "I'm going to " + what[num]
			filename = "discography.txt"
			fp = open(filename)
			JSON_string = fp.read()
			dd = json.loads(JSON_string)				# dictionary for the discography
			if num == 0:								
				print "Who's the artist?"				
				artist = raw_input("> ")
				print "So, you look for " + artist
				print "...wait..."
				res = disc.search_by_artist(artist, dd)
				if res:
					print res
				else:
					print "Artist not found"
			if num == 1:
				print "What's the title?"
				title = raw_input("> ")
				print "So, you look for " + title
				print "... wait..."
				res = disc.search_by_title(title, dd)
				if res:
					print res
				else: 
					print "Title not found"
			if num == 2:
				print "What's the year?"
				while True:
					raw_py = raw_input("> ")
					if raw_py.isdigit():
						py = int(raw_py)
						break
					else:
						print "Please, enter a number."					
				print "So, you look for " + raw_py
				print "...wait..."
				res = disc.search_by_publication_year(py, dd)
				if res:
					print res
				else:
					print "Publication Year not found"
			if num == 3:			
				print "How many tracks?"
				while True:
					raw_tt = raw_input("> ")
					if raw_tt.isdigit():
						tt = int(raw_tt)
						break
					else:
						print "Please, enter a number."
				print "So, you look for " + raw_tt
				print "...wait..."
				res = disc.search_by_total_tracks(tt, dd)
				if res:
					print res
				else:
					print "Not found"
			if num == 4:			
				print "Who's the artist?"				
				a = raw_input("> ")
				print "What's the title?"
				t = raw_input("> ")
				while True:
					print "What's the year?"
					raw_py = raw_input("> ")
					print "How many tracks?"
					raw_tt = raw_input("> ")
					if raw_tt.isdigit() and raw_py.isdigit():
						py = int(raw_py)
						tt = int(raw_tt)
						break
					else:
						print "Total tracks and publication year must be numbers. Try again!"
				print "...wait..."
				new_dd = disc.insert(a, t, py, tt, dd)
				fp.close()	
				fp = open(filename, 'w')								# truncate() doesn't work with open(filename, 'r+')
				new_JSON_string = json.dumps(new_dd)
				fp.write(new_JSON_string)

			if num == 5:
				# check if it works properly!
				res = disc.print_all(dd)
				print res

			if num == 6:		
				print "Bye"
				break

			fp.close()	
		else:
			print "Please, enter a correct number!"