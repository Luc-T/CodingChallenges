def number_length(num):
    size = 0
    while size < 31:
        size += 1
        num = num / 10
        if num < 1: return size

#print(number_length(777777777777777777777777777777))