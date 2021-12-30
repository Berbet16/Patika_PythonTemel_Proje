
input = eval(input("add a input :"))
output = []

def isSingle(t):
    if type(t) ==  str  or type(t) == float or type(t) == int:
        return True
    else:
        return False

def flatten(x):
    if isSingle(x):
        output.append(x)
    else:
        for i in x:
            flatten(i)

flatten(input)
print(output)
