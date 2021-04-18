#Create a function that takes an array of numbers and return "Boom!" if the digit 7 appears in the array. Otherwise, return "there is no 7 in the array".

def sevenBoom(list):
    numbers = ""
    numbers = numbers.join(str(list))
    print(numbers)
    if numbers.find('7') > -1:
        return "boom"
    else:
        return "there is no 7 in the array"


print(sevenBoom([1, 2, 3, 4, 5, 6, 7]))# ➞ "Boom!")


print(sevenBoom([8, 6, 33, 100]))# ➞ "there is no 7 in the array")


print(sevenBoom([2, 55, 60, 97, 86]))# ➞ "Boom!")