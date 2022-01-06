
input = eval(input("add a input :"))

def isList(t):
    if type(t) ==  list:
        
        return True
    else:
        
        return False

def reverse(x):
    if isList(x):
        for i,e in enumerate(x):
            if isList(e):
                x[i] = e[::-1]
        x = x[::-1]
    return x
    


print(reverse(input))

