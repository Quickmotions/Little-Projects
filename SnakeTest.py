#FERGUS HAAK 18/04/21
#https://edabit.com/challenge/Y5Ji2HDnQTX7MxeHt
#area of n*n
#food eaten doubles snake
#how many eats before out of space

def snakefill(n):
    squares = n*n
    length = 1
    counter = 0
    while length + length <= squares:
        counter += 1
        length = length + length
    return counter


print(snakefill(3))# ➞ 3)

print(snakefill(6))# ➞ 5)

print(snakefill(24))# ➞ 9)

print(snakefill(900))# ➞ 19)

print(snakefill(1))# ➞ 0)