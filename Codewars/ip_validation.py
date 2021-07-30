# FERGUS HAAK 30/07/21
# https://www.codewars.com/kata/515decfd9dcfc23bb6000006
# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format.
# IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.
# Examples of valid inputs:
# 1.2.3.4
# 123.45.67.89
# Examples of invalid inputs:
# 1.2.3
# 123.456.78.90

# my plan:

# split on dots
# determine if range of list is 3
# test each item in list is between 0 and 255

# my solution:
def is_valid_IP(string):
    string = string.split('.')
    if len(string) != 4:
        return False
    for item in string:
        try:
            for letter in item:
                if letter == ' ':
                    return False
            if int(item) > 255 or int(item) < 0:
                return False
            elif item[0] == '0' and len(item) > 1:
                return False
            else:
                pass
        except:
            return False
    return True


# most efficient solution:
def better_is_valid_IP(strng):
    lst = strng.split('.')
    passed = 0
    for sect in lst:
        if sect.isdigit():
            if sect[0] != '0':
                if 0 < int(sect) <= 255:
                    passed += 1
    return passed == 4


print(
    is_valid_IP('12.255.56.1'),
    is_valid_IP(''),
    is_valid_IP('abc.def.ghi.jkl'),
    is_valid_IP('123.456.789.0'),
    is_valid_IP('12.34.56'),
    is_valid_IP('12.34.56 .1'),
    is_valid_IP('123.045.067.089')
)
