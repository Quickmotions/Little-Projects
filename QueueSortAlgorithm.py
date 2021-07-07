from unittest import test
def queue_time(customers, n):
    t = 0
    largest = max(customers)
    if n > 0:
        
        for c in customers:
            n -= 1
            t += c
        
        
    return t

test.assert_equals(queue_time([], 1), 0, "wrong answer for case with an empty queue")
test.assert_equals(queue_time([5], 1), 5, "wrong answer for a single person in the queue")
test.assert_equals(queue_time([2], 5), 2, "wrong answer for a single person in the queue")
test.assert_equals(queue_time([1,2,3,4,5], 1), 15, "wrong answer for a single till")
test.assert_equals(queue_time([1,2,3,4,5], 100), 5, "wrong answer for a case with a large number of tills")
test.assert_equals(queue_time([2,2,3,3,4,4], 2), 9, "wrong answer for a case with two tills")

# There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!
# input

#     customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
#     n: a positive integer, the number of checkout tills.

# output

# The function should return an integer, the total time required.