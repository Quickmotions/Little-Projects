# FERGUS HAAK 20/07/21
def determinant(matrix):
    group_values = []
    print(matrix)
    for group in matrix:
        temp = 1
        for val in group:
            temp *= val
        group_values.append(temp)
    print(group_values)
    output = group_values[0]
    for num in group_values[1:]:
        output -= num
    return output

m1 = [ [1, 3], [2,5]]
m2 = [ [2,5,3], [1,-2,-1], [1, 3, 4]]
print(determinant(m1))
#print(determinant(m2))


# A 2x2 matrix [ [a, b], [c, d] ] 
# has determinant: a*d - b*c.