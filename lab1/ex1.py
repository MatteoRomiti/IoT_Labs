#everytime a computation is correctly executed, a .txt file is created
#everytime this script runs, it overrides the previous .txt files

import json
from calculator import Calculator1

if __name__ == "__main__":

	calc = Calculator1("calculator_1");
#	op = Operation("operation_1")
	n = 1 												# JSON_outputn.txt
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
					op1 = float(op1)
					op2 = float(op2)
					NaD = 0													
				else:
					print "That was not a number. Try again"

			if op == "add":
				res = calc.add(op1, op2)
			if op == "sub":
				res = calc.sub(op1, op2)
			if op == "mul":
				res = calc.mul(op1, op2)
			if op == "div":
				if op2 == 0:
					while op2 == 0:
						print "WARNING: second number can not be zero. Try another number: "
						op2 = float(raw_input("second number: ")) 
				res = calc.div(op1, op2)
			print op1, op, op2
			print "The result is: ", res

			s = str(n)
			filename = "JSON_output" + s + ".txt"
			fp = open(filename, 'w')
			fp.truncate()
			JSON_obj = {"operation": op,"operator1": op1,"operator2": op2, "result": res}
			JSON_string = json.dumps(JSON_obj)
			fp.write(JSON_string)
			fp.close()
			n = n+1

		else: 
			print "Please, select a proper operation"