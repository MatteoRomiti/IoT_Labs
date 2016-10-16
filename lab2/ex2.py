import cherrypy
import json
from calculator import Calculator1

class webcalc(object):
	exposed = True
	
	def __init__(self):
		self.calc = Calculator1("calculator_1");

	def GET (self, *uri, ** params):
		if len(uri) == 3 and len(params) == 0:
			op = uri[0]
			if uri[1].replace('.','',1).isdigit() and uri[2].replace('.','',1).isdigit(): # numbers
				op1 = float(uri[1])
				op2 = float(uri[2])
				if op == "add" or op == "sub" or op == "mul" or op == "div":
					if op == "add":
						res = self.calc.add(op1, op2)
					if op == "sub":
						res = self.calc.sub(op1, op2)
					if op == "mul":
						res = self.calc.mul(op1, op2)
					if op == "div":
						# if an http error occurs, its number and the string inside ZeroDivisionError() will be shown
						try:
							res = self.calc.div(op1, op2)
						except: 
							raise ZeroDivisionError("Division by zeroooooooooooooooo!")
					JSON_obj = {"operation": op,"operator1": op1,"operator2": op2, "result": res}
					JSON_string = json.dumps(JSON_obj)
					return JSON_string 
				else:
					return "Choose a proper operator!"
			else:
				return "Choose two numbers!"
		else: 
			return "Choose one operation and two numbers! Example: /add/3/2"
			
if __name__ == '__main__':
	conf = {
		'/': {
			'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
			'tools.sessions.on': True,
		}
	} 
	cherrypy.quickstart(webcalc(), '/', conf)