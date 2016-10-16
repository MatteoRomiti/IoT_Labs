import urllib2

if __name__ == "__main__":

	what = ["Get Temperature Info", "Get Humidity Info", "Toggle Relay Status", "Get Relay Status", "Exit"]

	while True:
		print "What do you want to do? Choose a number: "
		for i, v in enumerate(what):
			print i, v
		raw_num = raw_input("> ")
		if raw_num.isdigit():
			num = int(raw_num)
			if num == 3:		
				print "Bye"			
				break
			else:
				list_num = range(len(what))
				command = what[num].replace(' ', '_').lower()
				if num in list_num:
					url = "http://localhost:8080/" + command
					response = urllib2.urlopen(url)
					html = response.read()
					print html
				else: 
					print "Invalid number"
		else:
			print "Please enter a number"
