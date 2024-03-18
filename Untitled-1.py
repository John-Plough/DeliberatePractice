






def persistence(n):
def persistence(n):
    n = str(n)
    n = str(n)
    count = 0
    count = 0

    while len(n) > 1:
    while len(n) > 1:
        p = 1
        product = 1
        for i in n:
        for digit in n:    
            p *= int(i)
            product *= int(digit)
        n = str(p)
        count += 1
    
    return count

print(persistence(999))