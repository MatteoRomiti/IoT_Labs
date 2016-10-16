import urllib2

if __name__ == "__main__":

	choices = ["Sort by available slots",
	"Sort by available bikes",
	"Select by zipcode", 
	"Stations with more than n available ebikes",
	"Get the amount of bikes and slots in a district",
	"Exit"]

	choice_num = range(len(choices))
	while True:
		print "What do you want to do? Choose a number: "
		for i, v in enumerate(choices):
			print i, v
	 	raw_num = raw_input("> ")
	 	if raw_num.isdigit():
	 		num = int(raw_num)
	 		if num in choice_num:
		 		command =  choices[num].replace(' ', '_').lower()
		 		# always in the url
		 		n = "10"
		 		order = "1"
		 		zipcode = "0"
		 		zip_list = ["08013","08010","08003","08018","08005","08009","08025","08037","08002","08026","08001","08007","08029","08011","08008","08036","08015","08004","08014","08021","08024","08006","08020","08019","08041","08028","08034","08017","08012","08027","08030","08033","08016","08031","08032","08042","08022","08038","08098","08039","08023"]
				ne = "10"
				district = "0"
				district_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
				if num == 0 or num ==1:
					while True:
						print "How many stations do you want to see? Press Enter for default value 10"
						n = raw_input("> ")
						if not n: # N is empty
							n = "10"
							break
						elif n.isdigit():
							break
						else:
							print "Please, enter a number for the stations."
					while True:
						print "Choose a number: press Enter for default value 1"
						print "1 for descendent order "
						print "0 for ascendent order "
						order = raw_input("> ")
						if not order:
							order = "1"
							break
						elif order.isdigit():
							if int(order) in range(2):
								break
							else:
								print "Choose 0 or 1"
						else:
							print "Please, choose a number for the order"

				if num == 2:
					while True:
						print "Enter a zipcode: "
						zipcode = raw_input("> ")
						if zipcode.isdigit():
							if zipcode in zip_list:
								break
							else:
								print "Invalid zipcode, try again"
						else:
							print "Please, enter a number."
				
				if num == 3:
					while True:
						print "Enter the minimum number of bikes for a station with e-bikes: "
						ne = raw_input("> ")
						if ne.isdigit():
							break
						else:
							print "Please, enter a number."
				if num == 4:
					while True:
						print "Enter the number of the district: "
						district = raw_input("> ")
						if district in district_list:
							break
						else:
							print "Invalid number for district. Try again."

				if num == 5:		
					print "Bye"			
					break

				url = "http://localhost:8080/" + command + "?n=" + str(n) + "&order=" + str(order) + "&zipcode=" + str(zipcode) + "&ne=" + str(ne) + "&district=" + str(district)
				response = urllib2.urlopen(url)
				html = response.read()
				print html


			else:
				print "Please, choose a correct number."
	 	else:
	 		print "Please, choose a number."

