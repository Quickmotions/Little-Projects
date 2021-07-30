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
# deternime if range of list is 3
# test each item in list is between 0 and 255


def is_valid_IP(string):
    


print(
    is_valid_IP('12.255.56.1'),
    is_valid_IP(''),
    is_valid_IP('abc.def.ghi.jkl'),
    is_valid_IP('123.456.789.0'),
    is_valid_IP('12.34.56')
    )
