#FERGUS HAAK 18/04/21
def calculator(num1, operator, num2):
	try:
		return eval(str(num1) + operator + str(num2))
	except:
		return "Can't divide by 0!"

#main1
a = input("number 1: ")
b = input("operator: ")
c = input("number 2: ")
answer = calculator(a, b, c)
print("answer = " + str(answer))