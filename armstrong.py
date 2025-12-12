def armstrong(n):
    numstr = str(n)
    sum = 0
    for digit in numstr:
        sum += int(digit) ** 3
    return sum == n

n = int(input("Enter a number: "))
print(armstrong(n))