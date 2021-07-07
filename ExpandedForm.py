def expanded_form(num):
    s = ""
    v = len(list(str(num))) -1
    for idx, val in enumerate(list(str(num))):
        if val != "0":
            s +=(f"{int(val)}" + "0"*v) 
            if idx != len(list(str(num))) -1:
                s += " + "
        v -= 1
    if s[-3:] == " + ":
        s = s[:-3] 
    return s

#optimal solution

def optimal(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')

print(expanded_form(12))# '10 + 2'
print(expanded_form(420)) #'40 + 2'
print(expanded_form(70304)) #'70000 + 300 + 4'
print(expanded_form(9000)) #'9000'


#You will be given a number and you will need to return it as a string in Expanded Form. For example:
# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
