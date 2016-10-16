import urllib2
import json

if __name__ == "__main__":

	while True:
		print "Please select an operation:"
		print "add"
		print "sub"
		print "mul"
		print "div"
		print "Type 'exit' to close your calculator!"
		op = raw_input("---->")
		if op == "exit":
			print "Bye"
			break
		if op == "add" or op == "sub" or op == "mul" or op == "div":
			print "Great choice! Choose 2 numbers: "
			NaD = 1 									# Not a Digit: we assume that the user is a rascal
			while NaD:
				op1 = raw_input("first number: ")
				op2 = raw_input("second number: ")
				if op1.replace('.','',1).isdigit() and op2.replace('.','',1).isdigit():
					NaD = 0													
				else:
					print "That was not a number. Try again"

			# at this point op, op1 and op2 are correct input (exception: op2 can be zero) 
			url = "http://localhost:8080/" + op + "?op1=" + op1 + "&op2=" + op2
			response = urllib2.urlopen(url)
			html = response.read()
			# html is 100% a correct JSON string and a ZeroDivisionError would be in d["result"]
			d = json.loads(html)
			print "The result is: " + str(d["result"]) 
