import urllib2

if __name__ == "__main__":

	what = ["Print all", # GET
	"Search by artist", # GET
	"Search by title", # GET
	"Search by publication year", # GET
	"Search by total tracks", # GET
	"Insert a new album", # POST
	"Delete an album", # DELETE
	"Exit"]

	while True:
		print "What do you want to do? Choose a number: "
		for i, v in enumerate(what):
			print i, v
		raw_num = raw_input("> ")
		if raw_num.isdigit():
			num = int(raw_num)
			command = what[num]
			print "I'm going to " + command.lower()
			command = command.replace(' ', '_').lower()
			a = "null"
			t = "null"
			py = "0"
			tt = "0"

			if num == 0:
				print "So, you want to see the whole discography."

			if num == 1:								
				print "Who's the artist?"				
				a = raw_input("> ")
				print "So, you look for " + a

			if num == 2:
				print "What's the title?"
				t = raw_input("> ")
				print "So, you look for " + t

			if num == 3:
				print "What's the year?"
				while True:
					raw_py = raw_input("> ")
					if raw_py.isdigit():
						py = raw_py
						break
					else:
						print "Please, enter a number."					
				print "So, you look for " + raw_py

			if num == 4:			
				print "How many tracks?"
				while True:
					raw_tt = raw_input("> ")
					if raw_tt.isdigit():
						tt = raw_tt
						break
					else:
						print "Please, enter a number."
				print "So, you look for " + raw_tt

			if num == 5:			
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
						py = raw_py
						tt = raw_tt
						break
					else:
						print "Total tracks and publication year must be numbers (integers). Try again!"
			if num == 6:
				print "Who's the artist?"				
				a = raw_input("> ")
				print "What's the title?"
				t = raw_input("> ")
				# 
			if num == 7:		
				print "Bye"			
				break

			url = "http://localhost:8080/" + command + "?artist=" + a.replace(' ', '_') + "&title=" + t.replace(' ', '_') + "&py=" + py + "&tt=" + tt
			response = urllib2.urlopen(url)
			html = response.read()
			print html
		else:
			print "Please, enter a correct number!"