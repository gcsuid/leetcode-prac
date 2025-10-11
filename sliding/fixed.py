'''maxsum =0
curr = 0
for i in range(k):
    curr += arr[i]
    maxsum = curr
for i in range(k, len(arr)):
    curr += arr[i] - arr[i-k]
    maxsum = max(maxsum, curr)
return maxsum'''
    