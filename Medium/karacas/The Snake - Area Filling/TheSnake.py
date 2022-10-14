def snakefill(n):
    s = 1
    count = 0
    while s < n*n:
        count +=1
        s = s*2
    return count-1