import cherrypy
import json
from calculator import Calculator2
import copy

class webcalc(object):
	exposed = True
	
	def __init__(self):
		self.calc = Calculator2();

	def POST (self, *uri, ** params):
		JSON_string = cherrypy.request.body.read()
		try:
			d = json.loads(JSON_string)
			op = d["command"]
			list_num = d["operands"]
			# possible errors:
			# 1) d["command"] or d["operands"] don't exist
			# 2) d["operands"] contains at least one element which is not a number neither a string: [1, two, 3] won't be decoded as a JSON string, while [1, "two", 3] will
		except:
			raise KeyError("""The JSON string should be like this: {"command": "add", "operands": [2, 0, 3] }""")
			# using Postman you'll get the whole html page and not just the red error message

		if op == "add" or op == "sub" or op == "mul" or op == "div":
			# list_num may still contain a string of NaN, so check it!
			n = 0	# it'll increase for each number encountered in list_num
			for j in range(len(list_num)):					
				if str(list_num[j]).replace('.','',1).isdigit(): # need to cast list_num[j] to a string in order to use isdigit()
					list_num[j] = float(list_num[j])
					n += 1
				else:
					pass
			if n == len(list_num): 							# true if list_num has only numbers
				numbers = copy.copy(list_num)						# multi_div pops out the first number
				if op == "add":
					res = self.calc.multi_add(list_num)
				if op == "sub":
					res = self.calc.multi_sub(list_num)
				if op == "mul":
					res = self.calc.multi_mul(list_num)
				if op == "div":
					try:
						res = self.calc.multi_div(list_num)
					except:
						raise ZeroDivisionError("Division by zero is not allowed")
				JSON_obj = {"operation": op,"numbers": numbers, "result": res}
				JSON_string = json.dumps(JSON_obj)
				return JSON_string 
			else:
				return "Only numbers!"
		else:
			return "Choose a proper operator!"
			
if __name__ == '__main__':
	conf = {
		'/': {
			'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
			'tools.sessions.on': True,
		}
	}
	cherrypy.quickstart(webcalc(), '/', conf)