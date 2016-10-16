#!/usr/bin/python
#everytime a computation is correctly executed, a .txt file is created

import copy
import json
from calculator import Calculator2

if __name__ == "__main__":

	calc = Calculator2();
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
			print "Great choice! Enter the numbers : "	
			NaD = 1 									# Not a Digit: we assume that the user is a rascal
			while NaD:
				str_num = raw_input("----> ")
				list_num = str_num.split()
				for j in range(len(list_num)):					
					if list_num[j].replace('.','',1).isdigit(): 
						list_num[j] = float(list_num[j])
						if j == (len(list_num)-1):		# they are all numbers
							NaD = 0						
					else:
						print "Sorry, only numbers! Try again."
						break							# ends the for loop but is still inside the while loop => again raw_input() 
			numbers = copy.copy(list_num)				# multi_div and multi_sub pops out the first number
			if op == "add":
				res = calc.multi_add(list_num)
			if op == "sub":
				res = calc.multi_sub(list_num)
			if op == "mul":
				res = calc.multi_mul(list_num)
			if op == "div": 							
				if (0 in list_num) and (list_num.index(0) > 0):		# is there a "bad" zero?
					print "WARNING: you can't divide by zero! Try again. "
					break 											
				res = calc.multi_div(list_num)
				
			print "The result is: ", res

			s = str(n)
			filename = "JSON_output" + s + ".txt"
			fp = open(filename, 'w+')
			fp.truncate()
			JSON_obj = {"operation": op,"numbers": numbers, "result": res}
			JSON_string = json.dumps(JSON_obj)
			fp.write(JSON_string)
			fp.close()
			n = n+1

		else: 
			print "Please, select a proper operation"