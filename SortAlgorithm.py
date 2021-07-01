def sort(num):
    counter = len(num) -1
    for x in range(len(num) - 1):
        for x in range(counter):
            first = num[x]
            second = num[x+1]
            if int(first) > int(second):
                num = num[:x] + second + num[1+x:]
                num =num[:1+x] + first + num[2+x:]
        counter -= 1
    return num
print("My algorithm:    " + sort(input("Enter Number")))
