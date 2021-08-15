def binarySearch(arr, startAt, upto, elem):
    r = upto
    l = startAt - 1
    while (r - l > 1):
        m = l + (r - l)//2
        if (arr[m] > elem):
            r = m
        else:
            l = m
    return r


arr = [1, 1, 5, 7, 7,7, 7, 7]

print(binarySearch(arr, 0, len(arr),  1))
