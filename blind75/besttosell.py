def tosell(prices):
    #brute force
    '''n = len(prices)
    maxp = 0
    for i in range(n):
        for j in range(i+1,n):
            profit = j - i
            maxp = max(profit,maxp)
    return maxp'''

    n = len(prices)
    l,r = 0,1 #since using 2 pointers approach
    maxp = 0
    while r < n:
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxp = max(profit, maxp)
        else:
            l = r #if not equal, bring them to be equal.
        r += 1
    return maxp

li = list(map(int, input("enter numbers separated by a space:").split()))
print(tosell(li))


