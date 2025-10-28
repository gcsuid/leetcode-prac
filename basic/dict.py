'''d = {"a": 1, "b": 2}
d["c"] = 3      # insert
d["a"] = 10     # update
print(d.get("x", 0))  # safe lookup with default
print("b" in d)       # membership'''



'''names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")'''


# dict look up

'''seen = {}
for i, value in enumerate(nums):
    if value in seen:
        return True
    seen[value] = i
return False'''


#set look up
'''seen = set()
for i, value in enumerate(nums):
    if value in seen:
        return True
    else:
        seen.add(value)
return False'''


#count freq, return only if one occurrence
'''counts = {}
for value in nums:
    count[value]= counts.get(value, 0) + 1
for i,value in enumerate(nums):
    if counts[value] == 1:
        return i
return -1'''

