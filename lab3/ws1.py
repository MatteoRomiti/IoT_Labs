import cherrypy
import json
from calculator import Calculator1

class webcalc(object):
	exposed = True
	
	def __init__(self):
		self.calc = Calculator1("calculator_1");

	def GET (self, *uri, ** params):
		if len(uri) == 1 and len(params) == 2:
			op = uri[0]
			try:  
				op1 = float(params["op1"])
				op2 = float(params["op2"])
				# possible errors: 
				# 1) params["op1"] or params["op2"] don't exist
				# 2) params["op1"] or params["op2"] are not numbers
			except:
				return "Operands must be named: op1 and op2 and they must be numbers too!"
				# if this error is raised, the rest of the code won't be executed
			
			if op == "add" or op == "sub" or op == "mul" or op == "div": # correct operator
				if op == "add":
					res = self.calc.add(op1, op2)
				if op == "sub":
					res = self.calc.sub(op1, op2)
				if op == "mul":
					res = self.calc.mul(op1, op2)
				if op == "div":	
					try:
						res = self.calc.div(op1, op2)
					except: 
						#raise ZeroDivisionError("Division by zero is not allowed.")
						res = "ERROR: division by zero is not allowed."
				JSON_obj = {"operation": op,"operator1": op1,"operator2": op2, "result": res}
				JSON_string = json.dumps(JSON_obj)
				return JSON_string
			else:
				return "Choose a proper operator!"
		else: 
			return "Choose one operation and two numbers. Example: /add?op1=3&op2=2"
			
if __name__ == '__main__':
	conf = {
		'/': {
			'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
			'tools.sessions.on': True,
		}
	} 
	cherrypy.quickstart(webcalc(), '/', conf)