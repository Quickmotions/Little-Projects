def queue_time(customers, n):
    queue = []
    for till in range(n):
        queue.append(0)
    for customer in customers:
        minTill = 0
        for till in range(n):
            if queue[till] < queue[minTill]:
                minTill = till
        queue[minTill] += customer
    return max(queue)

#optimal solution

def optimal(customers, n):
    l=[0]*n
    for i in customers:
        l[l.index(min(l))]+=i
    return max(l)



print(queue_time([2,2,3,3,4,4], 2)) #9
print(queue_time([2], 5))#2
print(queue_time([1,2,3,4,5], 1)) #15
print(queue_time([1,2,3,4,5], 100)) #5

# There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!
# input

#     customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
#     n: a positive integer, the number of checkout tills.

# output

# The function should return an integer, the total time required.