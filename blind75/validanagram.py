def validanagaram(s,t):
    ct = {}
    cs = {}
    for i in s:
        cs[i] = cs.get(i,0) + 1
    for i in t:
        ct[i] = ct.get(i,0) + 1
    return cs == ct

# Example usage:
s = input("Enter first string: ")
t = input("Enter second string: ")
print(validanagaram(s,t))