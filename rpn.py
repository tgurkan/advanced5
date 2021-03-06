#!/usr/bin/python
#changes added
import readline
import operator
from colorama import init
init()
from colorama import Fore
def calculate(string):
	stack = list()
	operators = {
	'+' : operator.add, 
	'-' : operator.sub,
	'*' : operator.mul,
	'/' : operator.truediv,}
	for token in string.split():
		try:
			token = int(token)
			stack.append(token) #Add numbers only
		except ValueError:
			function = operators[token]
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = function(arg1, arg2)
			stack.append(result)
		print(stack)
	if len(stack) != 1:
		raise TypeError("Too many parameters")
	return stack.pop()

def main():
	while True:
		print(Fore.RED + calculate(input("rpn calc> ")))

if __name__ == '__main__': # Note that's "underscore underscore n a m e ..."
	main()


