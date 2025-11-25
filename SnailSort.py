array = [[1,2,3],
         [8,9,4],
         [7,6,5]]

"""
first line takes array[0] the array = [1:]
then pop left elements for len(array) pop [-1]
take bottom array[-1] then array = [:1]
take right most elements for len(array.reverse) pop[0]
repeat
"""

def snail(snail_map):
    order = []
    while len(snail_map) > 0:
        for n in snail_map[0]:
            order.append(n)
        snail_map = snail_map[1:]
        for x in range(len(snail_map)):
            order.append(snail_map[x][-1])
            snail_map[x].pop(-1)
        snail_map = list(reversed(snail_map))
        for x in range(len(snail_map)):
            snail_map[x] = list(reversed(snail_map[x]))
    return order 

if __name__ == "__main__":
    print(snail(array))
