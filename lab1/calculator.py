class Calculator1():

	def __init__(self, id):
		self.id = id

	def add (self, operator1=0, operator2=0):
		return operator1 + operator2
	def sub (self, operator1=0, operator2=0):
		return operator1 - operator2
	def mul (self, operator1=0, operator2=0):
		return operator1 * operator2
	def div (self, operator1=0, operator2=1):
		return operator1 / operator2

	def getID (self):
		return self.id

class Calculator2():
	
	def multi_add(self, args): 
		result = 0
		for x in args:
			result = result + x
		return result

	def multi_sub(self, args): 
		result = args.pop(0)
		for x in args:
			result = result - x
		return result

	def multi_mul(self, args): 
		result = 1
		for x in args:
			result = result * x
		return result

	def multi_div(self, args): 
		result = args.pop(0)
		for x in args:
			result = result / x
		return result