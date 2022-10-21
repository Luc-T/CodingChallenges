def is_disarium(num):
    sum = 0

    for count, n in enumerate(str(num), 1):
        sum += int(n)**count

    return (num == sum)