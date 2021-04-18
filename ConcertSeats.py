#https://edabit.com/challenge/xbjDMxzpFcsAWKp97
## FRONT STAGE
#[[1, 2, 3, 2, 1, 1],
#[2, 4, 4, 3, 2, 2],
#[5, 5, 5, 5, 4, 4],
#[6, 6, 7, 6, 5, 5]]

# Starting from the left, the 6 > 5 > 2 > 1, so all numbers can see.
# 6 > 5 > 4 > 2 - so all numbers can see, etc.
#Create a function that determines whether each seat can "see" the front-stage. A number can "see" the front-stage if it is strictly greater than the number before it.

#code
def can_see_stage(seats):
    for amountRow in range(len(seats)):
        column = []
        for row in seats:
            column.append(row[amountRow])
        if column != sorted(column):
            return False
    return True


#tests
print(can_see_stage([
  [0, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
]))# ➞ True
print(can_see_stage([
  [2, 1, 0], 
  [1, 1, 1], 
  [2, 2, 2]
])) #➞ False
print(can_see_stage(
[[1, 1, 3, 2, 1, 1], 
[2, 4, 4, 3, 2, 2], 
[5, 5, 5, 5, 4, 4], 
[6, 6, 7, 9, 5, 5]]))# True)