#FERGUS HAAK 18/04/21
#multiply num by all numbers lower than its self till 1
def factorial(num):
	factoral = num -1
	while factoral > 0:
		num *= factoral
		factoral -= 1
	return num
    #also works with 	return math.factorial(num) using import math
#main
num = int(input("num = "))
num = factorial(num)
print(num)
