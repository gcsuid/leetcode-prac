a, b = 6,9
print("before swap:", a, b)
a ^= b
b ^= a  
a ^= b
print("after swap:", a, b)